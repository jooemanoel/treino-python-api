#app/services/usuario_service.py

from app.dao.usuario_dao import obter_todos_usuarios

def listar_usuarios():
    return obter_todos_usuarios()

from app.dao.usuario_dao import inserir_usuario

def criar_usuario(nome, senha):
    return inserir_usuario(nome, senha)
