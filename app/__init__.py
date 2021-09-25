from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from app.views import HelloWorld
from tutorial.config import Config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    api = Api(app)
    api.add_resource(HelloWorld, '/')
    db.init_app(app)
    return app
