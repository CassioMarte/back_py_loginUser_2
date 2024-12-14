from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):  # Classe base para representar um usuário
    email: EmailStr  # Valida se o email é válido

class UserCreate(UserBase):  # Herda de UserBase
    password: str  # Adiciona o campo de senha

class UserResponse(UserBase):  # Herda de UserBase
    id: int  # ID retornado para o cliente

    class Config:  # Configuração adicional para compatibilidade com ORMs
        orm_mode = True

class Token(BaseModel):  # Esquema para o token de autenticação
    access_token: str
    token_type: str


"""
 schema é um sistema de validação usando pydantic (simular ao zod e ao joi)

 e usa tipagem declarada similar ao typescript

BaseModel: Classe base do Pydantic.
UserCreate: Esquema para entrada de dados.
UserResponse: Esquema para saída, com mapeamento orm_mode para modelos ORM.

 
"""