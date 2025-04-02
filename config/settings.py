import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///logs/api_logs.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY")
    
    # Credenciais da API
    BITRIX_URL_API = os.getenv("BITRIX_URL_API")
    USERNAME_GENIAL = os.getenv("USERNAME_GENIAL")
    PASSWORD_GENIAL = os.getenv("PASSWORD_GENIAL")
    
    # Banco de Dados SQL Server
    SERVER_DB = os.getenv("SERVER_DB")
    USERNAME_DB = os.getenv("USERNAME_DB")
    PASSWORD_DB = os.getenv("PASSWORD_DB")
    DATABASE_DB = os.getenv("DATABASE_DB")