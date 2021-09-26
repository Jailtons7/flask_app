from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate

from app.models import db
from app.views import HelloWorld
from tutorial.config import Config

migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    api = Api(app)
    api.add_resource(HelloWorld, '/')
    db.init_app(app)
    migrate.init_app(app, db)
    return app
