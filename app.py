from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():

    app = Flask(__name__,template_folder="templates",static_folder="public",static_url_path="/")
    app.config['SQLALCHEMY_DATABASE_URI']="postgresql://postgres:root@localhost:5432/blog_app"
    db.init_app(app)

    # all imports
    from routes.auth import authRoutes
    from routes.blogs import blog_routes
    from context_processor.context_processor import inject

    # all routes
    authRoutes(app,db)
    blog_routes(app,db)

    app.context_processor(inject)
    Migrate(app,db)
    return app