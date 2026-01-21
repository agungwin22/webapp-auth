from flask import Flask
from app.extensions import db, login_manager
from config import Config


def mainloop():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app) # code ini berfungsi menghubungkan DB ke Flask

    from app.auth.routes import main
    app.register_blueprint(main)

    login_manager.init_app(app)
    login_manager.login_view = "login"

    return app