# back_py_loginUser_2

user_auth_backend/
│
├── app/
│   ├── __init__.py
│   ├── main.py            # Ponto de entrada da aplicação
│   ├── config.py          # Configurações da aplicação
│   ├── database.py        # Conexão e gerenciamento do banco de dados
│   ├── models.py          # Modelos do SQLAlchemy
│   ├── schemas.py         # Esquemas Pydantic (validação e tipagem)
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── routes.py      # Rotas de autenticação
│   │   ├── services.py    # Lógica de autenticação (hashing e geração de tokens)
│   │   ├── dependencies.py # Middleware de autenticação
│   └── utils/
│       └── __init__.py    # Utilitários gerais
│
├── requirements.txt       # Dependências do projeto
└── .env                   # Variáveis de ambiente

https://chatgpt.com/c/675bd77c-7170-8005-8fd6-cd2380a354bc



Crie um ambiente virtual no diretório do projeto
python -m venv venv


Ative o ambiente virtual
venv\Scripts\activate    ou   source venv/bin/activate


No diretório do seu projeto, crie um arquivo chamado
 requirements.txt

 coloque : 
   fastapi
   uvicorn
   sqlalchemy
   pydantic
   python-dotenv
   bcrypt
   python-jose[cryptography]



No terminal do VSCode, certifique-se de que o ambiente virtual está ativado e execute o seguinte comando:
pip install -r requirements.txt


Verifique se as dependências foram instaladas corretamente:
pip freeze



teste:
main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


database.py:
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

model.py
from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)



schema.py
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str
