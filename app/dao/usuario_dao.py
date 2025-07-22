# app/dao/usuario_dao.py

from app.db import get_connection
from app.models.usuario_model import Usuario

def obter_todos_usuarios():
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT id_usuario, nome, senha FROM usuarios")
            rows = cursor.fetchall()
            return [Usuario(id_usuario=row[0], nome=row[1], senha=row[2]) for row in rows]

def inserir_usuario(nome, senha):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO usuarios (nome, senha) VALUES (UPPER(%s), %s) RETURNING id_usuario",
                (nome, senha)
            )
            novo_id = cursor.fetchone()[0]
            conn.commit()
            return Usuario(id_usuario=novo_id, nome=nome, senha=senha)

def deletar_usuario(id_usuario):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM usuarios WHERE id_usuario = %s", (id_usuario,))
            conn.commit()
            return cursor.rowcount > 0  # True se algo foi apagado

def atualizar_usuario(id_usuario, nome, senha):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "UPDATE usuarios SET nome = UPPER(%s), senha = %s WHERE id_usuario = %s",
                (nome, senha, id_usuario)
            )
            conn.commit()
            return cursor.rowcount > 0  # True se algo foi atualizado

def buscar_usuario_por_id(id_usuario):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT id_usuario, nome, senha FROM usuarios WHERE id_usuario = %s", (id_usuario,))
            row = cursor.fetchone()
            if row:
                return Usuario(id_usuario=row[0], nome=row[1], senha=row[2])
            return None

def autenticar_usuario(nome, senha):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT id_usuario, nome, senha FROM usuarios WHERE nome = UPPER(%s) AND senha = %s",
                (nome, senha)
            )
            row = cursor.fetchone()
            if row:
                return Usuario(id_usuario=row[0], nome=row[1], senha=row[2])
            return None