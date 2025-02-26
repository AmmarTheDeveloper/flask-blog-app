from app import db

class Blog(db.Model):
    __tablename__ = "blog"
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255),nullable=False)
    content = db.Column(db.String(1000),nullable=False)
    thumbnail = db.Column(db.String(255),nullable=False)
    created_at = db.Column(db.DateTime,server_default=db.func.now())
    created_by = db.Column(db.Integer,db.ForeignKey("user.id"))
    author =  db.relationship("User")
