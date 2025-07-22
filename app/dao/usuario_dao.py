from app.db import get_connection

def obter_todos_usuarios():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id_usuario, nome, senha FROM usuarios")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    # Retornar como lista de dicionários ou objetos
    return [{"id": r[0], "nome": r[1], "senha": r[2]} for r in rows]
