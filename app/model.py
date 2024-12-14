from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base): #Base vem de database do SQLAlchemy conexão com o banco
    __tablename__ = "users"    # nome da tabela 
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)


"""
contem o modelo do banco de dados 
similar ao model do typeorm 

import { Entity, PrimaryGeneratedColumn, Column } from "typeorm"

@Entity('users')
export class User{
  @PrimaryGeneratedColumn()
   id: number

  @Column({unique: true })
  email: string

  @Column()
  hash_pass: string
}

"""