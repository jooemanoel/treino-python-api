#app/routes/usuario_routes.py

from flask import Blueprint, request, jsonify
from app.services.usuario_service import editar_usuario, listar_usuarios, criar_usuario, login_usuario, obter_usuario, remover_usuario

usuario_bp = Blueprint("usuario", __name__)

@usuario_bp.route("/", methods=["GET"])
def get_usuarios():
    try:
        usuarios = listar_usuarios()
        return jsonify([u.to_dict() for u in usuarios]), 200
    except LookupError as e:
        return jsonify({"erro": str(e)}), 404

@usuario_bp.route("/", methods=["POST"])
def post_usuario():
    dados = request.get_json()
    try:
        novo_usuario = criar_usuario(dados.get("nome"), dados.get("senha"))
        return jsonify(novo_usuario.to_dict()), 201
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400

@usuario_bp.route("/<int:id_usuario>", methods=["DELETE"])
def delete_usuario(id_usuario):
    try:
        remover_usuario(id_usuario)
        return jsonify({"mensagem": "Usuário apagado com sucesso"}), 200
    except LookupError as e:
        return jsonify({"erro": str(e)}), 404
    except Exception as e:
        return jsonify({"erro": str(e)}), 400

@usuario_bp.route("/<int:id_usuario>", methods=["PUT"])
def put_usuario(id_usuario):
    dados = request.get_json()
    try:
        editar_usuario(id_usuario, dados.get("nome"), dados.get("senha"))
        return jsonify({"mensagem": "Usuário atualizado com sucesso"}), 200
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400
    except LookupError as e:
        return jsonify({"erro": str(e)}), 404

@usuario_bp.route("/<int:id_usuario>", methods=["GET"])
def get_usuario_por_id(id_usuario):
    try:
        usuario = obter_usuario(id_usuario)
        return jsonify(usuario.to_dict()), 200
    except LookupError as e:
        return jsonify({"erro": str(e)}), 404
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400

@usuario_bp.route("/login", methods=["POST"])
def login():
    dados = request.get_json()
    try:
        usuario = login_usuario(dados.get("nome"), dados.get("senha"))
        return jsonify(usuario.to_dict()), 200
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400
    except PermissionError as e:
        return jsonify({"erro": str(e)}), 401