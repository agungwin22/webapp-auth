from flask import Flask
from config import Config
from app.auth.routes import main

def mainloop():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(main)
    return app