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


reiniciar projeto:
   python -m venv venv
   source venv/bin/activate


service.py
  from passlib.context import CryptContext
  from jose import JWTError, jwt
  from datetime import datetime, timedelta

  SECRET_KEY = "sua-chave-secreta"
  ALGORITHM = "HS256"
  ACCESS_TOKEN_EXPIRE_MINUTES = 30

  pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

  def hash_password(password: str) -> str:
    return pwd_context.hash(password)

  def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

  def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


route.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import UserCreate, UserResponse, Token
from app.models import User
from app.database import get_db
from app.auth.services import hash_password, verify_password, create_access_token

router = APIRouter()

@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    user_exists = db.query(User).filter(User.email == user.email).first()
    if user_exists:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = User(email=user.email, hashed_password=hash_password(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/login", response_model=Token)
def login_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = create_access_token(data={"sub": db_user.email})
    return {"access_token": token, "token_type": "bearer"}
