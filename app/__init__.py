from flask import Flask
from .config import config
from app.blueprints.main import main as main_blueprint
from app.blueprints.auth import auth as auth_blueprint


def create_app(config_name="default"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)

    return app
