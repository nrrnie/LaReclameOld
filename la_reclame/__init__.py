from flask import Flask


def create_app():
    app = Flask(__name__)

    from la_reclame.auth import auth
    app.register_blueprint(auth, url_prefix='/auth')

    return app
