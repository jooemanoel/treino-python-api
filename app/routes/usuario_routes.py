#app/routes/usuario_routes.py

from flask import Blueprint, request, jsonify
from app.services.usuario_service import listar_usuarios, criar_usuario

usuario_bp = Blueprint("usuario", __name__)

@usuario_bp.route("/", methods=["GET"])
def get_usuarios():
    usuarios = listar_usuarios()
    return jsonify([u.to_dict() for u in usuarios])

@usuario_bp.route("/", methods=["POST"])
def post_usuario():
    dados = request.get_json()

    nome = dados.get("nome")
    senha = dados.get("senha")

    if not nome or not senha:
        return jsonify({"erro": "Nome e senha são obrigatórios"}), 400

    novo_usuario = criar_usuario(nome, senha)
    return jsonify(novo_usuario.to_dict()), 201
