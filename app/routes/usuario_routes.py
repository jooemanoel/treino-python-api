from flask import Blueprint, request, jsonify
from app.services.usuario_service import listar_usuarios

usuario_bp = Blueprint("usuario", __name__)

@usuario_bp.route("/", methods=["GET"])
def get_usuarios():
    usuarios = listar_usuarios()
    return jsonify(usuarios)
