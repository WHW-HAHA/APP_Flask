from flask import Flask
from app.models.sql_book import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure') # Configure the app with the settings in secure and setting modules
    app.config.from_objetc('app.string') 
    register_blueprint(app)
    return app

def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)