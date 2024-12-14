# import express from 'express'
from fastapi import FastAPI

# conexão com banco
from app.database import Base, engine

#autenticação
from app.auth.routes import router as auth_router

# const app = express()
app = FastAPI()


#app.get('/', (req, res)=> res.send('Hello, express'))
@app.get("/")
def read_root():
    return {"message": "Hello, FASTAPI"}


 # Cria tabelas no banco de dados
Base.metadata.create_all(bind=engine) 

# Inclui as rotas de autenticação
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])  


"""
similar ao index ou a server no express

ponto de entrada da aplicação 

Inicializa a aplicação FastAPI, registra rotas e configurações, e inicia o servidor.

"""