# app/config.py

import os
from dotenv import load_dotenv

load_dotenv()  # Carrega variáveis do arquivo .env

class Config:
    DB_USER = os.getenv("user")
    DB_PASSWORD = os.getenv("password")
    DB_HOST = os.getenv("host")
    DB_PORT = os.getenv("port")
    DB_NAME = os.getenv("dbname")

    DEBUG = os.getenv("debug", "false").lower() == "true"
    SECRET_KEY = os.getenv("secret_key", "default-secret")
