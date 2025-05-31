from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)

    tarefas = relationship("Tarefa", back_populates="dono")


class Tarefa(Base):
    __tablename__ = "tarefas"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    descricao = Column(String, nullable=True)
    concluida = Column(Boolean, default=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))

    dono = relationship("Usuario", back_populates="tarefas")
