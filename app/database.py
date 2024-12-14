from sqlaachemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

#cria a conexão com o banco de dados  create_engine
engine = create_engine("DATABASE_URL", connect_args={"check_same_thread": False}) 

#Gera sessões para interagir com o banco, equivalente ao db.query no Knex.js.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Classe base para todos os modelos do SQLAlchemy.
Base = declarative_base()

#Fornece uma sessão do banco para ser usada em rotas, similar a um middleware de conexão.
#obs def = function
def get_db():
    db = SessionLocal()
    try:
        yield db  #yield diferente do return que conclui uma função yield só pausa e pode retornar de onde parou
    finally:
        db.close()

"""
configuração da conexão com banco de dados 

neste caso usando sqlalchemy.orm que é similar ao typeorm ou o knex

create_engine: Cria a conexão com o banco de dados.
SessionLocal: Gera sessões para interagir com o banco, equivalente ao db.query no Knex.js.
Base: Classe base para todos os modelos do SQLAlchemy.
get_db: Fornece uma sessão do banco para ser usada em rotas, similar a um middleware de conexão.

"""