#app/__init__.py

from flask import Flask
from app.routes.usuario_routes import usuario_bp
from app.routes.main_routes import main_bp
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(main_bp)
    app.register_blueprint(usuario_bp, url_prefix="/usuarios")

    return app
