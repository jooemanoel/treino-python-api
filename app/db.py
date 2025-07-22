# app/db.py

from psycopg2 import connect
from app.config import Config

def get_connection():
    config = Config()
    try:
        return connect(
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            host=config.DB_HOST,
            port=config.DB_PORT,
            dbname=config.DB_NAME
        )
    except Exception as e:
        print(f"Erro ao conectar: {e}")
        raise
