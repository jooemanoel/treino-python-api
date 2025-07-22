from flask import Flask
from app.routes.usuario_routes import usuario_bp
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Registrar rotas (blueprints)
    app.register_blueprint(usuario_bp, url_prefix="/usuarios")

    return app
