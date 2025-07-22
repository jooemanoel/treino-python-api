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
                "INSERT INTO usuarios (nome, senha) VALUES (%s, %s) RETURNING id_usuario",
                (nome, senha)
            )
            novo_id = cursor.fetchone()[0]
            conn.commit()
            return Usuario(id_usuario=novo_id, nome=nome, senha=senha)
