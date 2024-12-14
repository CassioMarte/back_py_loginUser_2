from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta

SECRET_KEY = "sua-chave-secreta"  # Chave secreta para assinar tokens
ALGORITHM = "HS256"  # Algoritmo para assinar os tokens
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Tempo de expiração do token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")  # Configuração para hashing

# Função para hashear senhas
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Função para verificar senhas
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# Função para criar um token JWT
def create_access_token(data: dict):
    to_encode = data.copy()  # Cria uma cópia dos dados fornecidos
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})  # Adiciona tempo de expiração
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
