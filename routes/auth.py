from flask import request,render_template,redirect,session
from models.user import User
from helper.message import Message
import json
from decorators.auth import login_required,logout_required
import json

def authRoutes(app,db):
    @app.route("/login",methods=['GET','POST'])
    @logout_required
    def login():
        if request.method == 'GET':
            return render_template("login.html",message=None)
        else:
            message = None
            try:
                if not "email" in request.form or not "password" in request.form:
                    raise Exception("All fields are required")

                email = request.form['email']
                password = request.form['password']
                user = User.query.filter(User.email == email).first()

                if not user or user.password != password:
                    raise Exception("Enter valid email and password")
                print(user)
                session['user'] = json.dumps(user.to_dict())
                message = Message("Logged in successfully...","success","alert-success")
                return render_template("login.html",message=message)
            except Exception as e:
                message = Message(str(e),"error","alert-danger")
                return render_template("login.html",message=message)

    @app.route("/register",methods=['GET','POST'])
    @logout_required
    def register():
        if request.method == 'GET':
            return render_template("register.html",message=None)
        else:
            message = None
            try:
                if not "name" in request.form or not "email" in request.form or not "password" in request.form or not "gender" in request.form:
                    raise Exception("All fields are required")
                name = request.form['name']
                email = request.form['email']
                password = request.form['password']
                gender = request.form['gender']

                user = User(name=name,email=email,gender=gender,password=password)
                db.session.add(user)
                db.session.commit()
                message = Message("Registered successfully","success","alert-success")
                return render_template("register.html",message=message)
            except Exception as e:
                db.session.rollback()
                msg = str(e)
                if "already exists" in str(e) or "unique constraint" in str(e):
                    msg = "Email already exists"
                message = Message(msg,"error","alert-danger")
                return render_template("register.html",message=message)

    @app.route("/logout")
    @login_required
    def logout():
        session['user'] = None
        return redirect("/login")