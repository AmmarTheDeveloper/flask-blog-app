from flask import render_template,request,session
from helper.message import Message
from helper.helper import isImage,saveFile,deleteFile
from models.blog import Blog
from models.user import User
import json
from decorators.auth import login_required
from helper.helper import getUser

def blog_routes(app,db):
    @app.route("/")
    @login_required
    def home():
        blogs = Blog.query.all()
        return render_template("index.html",blogs=blogs)

    @app.route("/blog/<int:id>")
    @login_required
    def blog(id):
        blog = Blog.query.filter(Blog.id == id).first()
        if not blog:
            message = Message("Blog you are searching for might have been deleted or doesn't exist.","error","alert-danger")
            blogs = Blog.query.all()
            return render_template("index.html",message=message,blogs=blogs)
        else:
            return render_template("blog.html",blog=blog)

    @app.route("/myblogs")
    @login_required
    def myblogs():
        user = getUser()
        blogs = Blog.query.filter(Blog.created_by == user.get("id")).all()
        return render_template("myblogs.html",blogs=blogs)

    @app.route("/blog/delete/<int:id>")
    @login_required
    def delete_blog(id):
        message = None
        user = getUser()
        blogs = None
        try:
            blog = Blog.query.filter(Blog.id == id).first()
            is_deleted = Blog.query.filter(Blog.id == id).delete()
            if is_deleted == 0:
                raise Exception('Blog not found to delete')
            if not deleteFile(blog.thumbnail):
                raise Exception("Blog image not deleted something went wrong")
            db.session.commit()
            message = Message("Blog deleted successfully","success","alert-success")
            blogs = Blog.query.filter(Blog.created_by == user.get("id")).all()
        except Exception  as e:
            blogs = Blog.query.filter(Blog.created_by == user.get("id")).all()
            db.session.rollback()
            message = Message(str(e),"error","alert-danger")
        return render_template("myblogs.html",message=message,blogs=blogs)

    @app.route("/blog/edit/<int:id>",methods=['GET','POST'])
    @login_required
    def update_blog(id):
        blog = Blog.query.filter(Blog.id == id).first()
        if not blog:
            user = getUser()
            blogs = Blog.query.filter(Blog.created_by == user.get("id")).all()
            message = Message("Blog not found to update","error","alert-danger")
            return render_template("myblogs.html",message=message,blogs=blogs)

        if request.method == 'GET':
            return render_template("update-blog.html",blog=blog)
        else:
            message = None
            try:
                if not "title" in request.form or not "content" in request.form:
                    raise Exception("Title and Content is required")
                title = request.form['title']
                content = request.form['content']
                filename = blog.thumbnail
                if "thumbnail" in request.files and request.files['thumbnail'].filename != "":
                    thumbnail = request.files['thumbnail']
                    if not isImage(thumbnail):
                        raise Exception("Invalid thumbnail provided, image is expected")

                    if not deleteFile(filename):
                        raise Exception("Previous thumbnail not deleted")
                    filename = saveFile(thumbnail)
                is_updated = Blog.query.filter(Blog.id == id).update({"title" : title,"content":content,"thumbnail":filename})
                print(is_updated)
                db.session.commit()
                message = Message("Blog updated successfully","success","alert-success")
            except Exception as e:
                db.session.rollback()
                message = Message(str(e), "error","alert-danger")
            return render_template("update-blog.html",message=message,blog=blog)


    @app.route("/add-blog",methods=['GET','POST'])
    @login_required
    def add_blog():
        if request.method == "GET":
            return render_template("add-blog.html",message=None)
        else:
            message = None
            try:
                if not "title" in request.form  or not "content" in request.form or not "thumbnail" in  request.files:
                    raise Exception("All fields are required")
                title = request.form['title']
                content = request.form['content']
                thumbnail = request.files['thumbnail']

                if thumbnail.filename == "":
                    raise Exception("Thumbnail is required")

                if not isImage(thumbnail):
                    raise Exception("Thumbnail should be image...")

                filename = saveFile(thumbnail)
                user = json.loads(session.get("user"))
                # user = User.query.get(dictUser.id)

                if not user:
                    raise Exception("User not found")

                blog = Blog(title=title,content=content,thumbnail=filename,created_by=user.get("id"))

                db.session.add(blog)
                db.session.commit()
                message = Message("Blog saved successfully","success","alert-success")
                return render_template("add-blog.html",message=message)
            except Exception as e:
                msg = str(e)
                if "value too long" in msg:
                    msg = "Blog content is too long"
                db.session.rollback()
                message = Message(msg,"error","alert-danger")
                return render_template("add-blog.html",message=message)