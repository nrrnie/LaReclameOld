from flask import Flask, redirect, url_for, render_template
from flask_session import Session
from config import Config

sess = Session()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    sess.init_app(app)

    from la_reclame.auth import auth
    app.register_blueprint(auth, url_prefix='/auth')
    from la_reclame.users import users
    app.register_blueprint(users, url_prefix='/users')
    from la_reclame.items import items
    app.register_blueprint(items, url_prefix='/items')

    @app.route('/')
    def main():
        return redirect(url_for('auth.login'))

    return app
