"""
similar ao dotenv

define configurações globais como variaveis de ambiente
"""

import os

class Config:
    # Configurações gerais
    APP_NAME = "Minha API"
    DEBUG = False
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///default.db")

class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URL = "sqlite:///dev.db"

class ProductionConfig(Config):
    DATABASE_URL = os.getenv("DATABASE_URL")

# Escolha a configuração com base no ambiente
def get_config():
    env = os.getenv("APP_ENV", "development")
    if env == "production":
        return ProductionConfig()
    return DevelopmentConfig()

"""
acessando dados do config

from config import get_config
config = get_config()
print(config.DATABASE_URL)

"""





"""
.env no python

APP_ENV=development
DATABASE_URL=sqlite:///dev.db
SECRET_KEY=supersecretkey
 


acessando 

from dotenv import load_dotenv
import os

load_dotenv()  # Carrega as variáveis do arquivo .env

# Acessando variáveis de ambiente
app_env = os.getenv("APP_ENV")
db_url = os.getenv("DATABASE_URL")
secret_key = os.getenv("SECRET_KEY")

print(f"Ambiente: {app_env}, Banco: {db_url}")

"""