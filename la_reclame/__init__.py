from flask import Flask
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from la_reclame.auth import auth
    app.register_blueprint(auth, url_prefix='/auth')
    from la_reclame.users import users
    app.register_blueprint(users, url_prefix='/users')

    return app
