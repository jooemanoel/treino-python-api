#app/services/usuario_service.py

from app.dao.usuario_dao import atualizar_usuario, autenticar_usuario, buscar_usuario_por_id, deletar_usuario, inserir_usuario, obter_todos_usuarios

def listar_usuarios():
    usuarios = obter_todos_usuarios()
    if not usuarios:
        raise LookupError("Nenhum usuário encontrado")
    return usuarios

def criar_usuario(nome, senha):
    if not nome or not senha:
        raise ValueError("Nome e senha são obrigatórios")
    return inserir_usuario(nome, senha)

def remover_usuario(id_usuario):
    if not id_usuario:
        raise ValueError("ID é obrigatório")
    sucesso = deletar_usuario(id_usuario)
    if not sucesso:
        raise LookupError("Usuário não encontrado")

def editar_usuario(id_usuario, nome, senha):
    if not nome or not senha:
        raise ValueError("Nome e senha são obrigatórios")
    sucesso = atualizar_usuario(id_usuario, nome, senha)
    if not sucesso:
        raise LookupError("Usuário não encontrado")

def obter_usuario(id_usuario):
    if not id_usuario:
        raise ValueError("ID é obrigatório")
    usuario = buscar_usuario_por_id(id_usuario)
    if not usuario:
        raise LookupError("Usuário não encontrado")
    return usuario

def login_usuario(nome, senha):
    if not nome or not senha:
        raise ValueError("Nome e senha são obrigatórios")
    usuario = autenticar_usuario(nome, senha)
    if not usuario:
        raise PermissionError("Credenciais inválidas")
    return usuario