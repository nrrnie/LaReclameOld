from flask import Flask


def create_app():
    app = Flask(__name__)

    from la_reclame.auth import auth
    app.register_blueprint(auth, url_prefix='/auth')
    from la_reclame.users import users
    app.register_blueprint(users, url_prefix='/users')
    from la_reclame.items import items
    app.register_blueprint(items, url_prefix='/items')

    return app
