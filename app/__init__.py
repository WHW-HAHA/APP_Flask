from flask import Flask

def create_app():
    app = Flask(__name__)  # with a name
    app.config.from_object('config')  # path of the module
    register_blueprint(app)
    return app

def register_blueprint(app):
    #
    from app.web.book import web
    app.register_blueprint(web)