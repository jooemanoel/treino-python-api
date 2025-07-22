# db.py (revisado com config)
from psycopg2 import connect
from app.config import Config

def get_connection():
    try:
        return connect(
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            host=Config.DB_HOST,
            port=Config.DB_PORT,
            dbname=Config.DB_NAME
        )
    except Exception as e:
        print(f"Erro ao conectar: {e}")
        raise
