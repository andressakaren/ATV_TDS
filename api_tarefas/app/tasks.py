from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from app import database, models, utils

from pydantic import BaseModel
from typing import Optional, List

router = APIRouter(prefix="/tasks")

security = HTTPBearer()

SECRET_KEY = utils.SECRET_KEY
ALGORITHM = "HS256"

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_usuario_logado(credenciais: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    token = credenciais.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = int(payload.get("sub"))
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")

    usuario = db.query(models.Usuario).filter(models.Usuario.id == user_id).first()
    if not usuario:
        raise HTTPException(status_code=401, detail="Usuário não encontrado")
    return usuario

class TarefaCriar(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    
class TarefaMostrar(BaseModel):
    id: int
    titulo: str
    descricao: Optional[str]
    concluida: bool

    class Config:
        orm_mode = True

@router.post("/", response_model=TarefaMostrar)
def criar_tarefa(dados: TarefaCriar, db: Session = Depends(get_db), usuario = Depends(get_usuario_logado)):
    nova = models.Tarefa(
        titulo=dados.titulo,
        descricao=dados.descricao,
        usuario_id=usuario.id
    )
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

@router.get("/", response_model=List[TarefaMostrar])
def listar_tarefas(db: Session = Depends(get_db), usuario = Depends(get_usuario_logado)):
    return db.query(models.Tarefa).filter_by(usuario_id=usuario.id).all()


class TarefaAtualizar(BaseModel):
    titulo: Optional[str]
    descricao: Optional[str]
    concluida: Optional[bool]

@router.put("/{tarefa_id}", response_model=TarefaMostrar)
def atualizar_tarefa(tarefa_id: int, dados: TarefaAtualizar, db: Session = Depends(get_db), usuario = Depends(get_usuario_logado)):
    tarefa = db.query(models.Tarefa).filter_by(id=tarefa_id, usuario_id=usuario.id).first()
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    if dados.titulo is not None:
        tarefa.titulo = dados.titulo
    if dados.descricao is not None:
        tarefa.descricao = dados.descricao
    if dados.concluida is not None:
        tarefa.concluida = dados.concluida

    db.commit()
    db.refresh(tarefa)
    return tarefa

@router.delete("/{tarefa_id}")
def deletar_tarefa(tarefa_id: int, db: Session = Depends(get_db), usuario = Depends(get_usuario_logado)):
    tarefa = db.query(models.Tarefa).filter_by(id=tarefa_id, usuario_id=usuario.id).first()
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    
    db.delete(tarefa)
    db.commit()
    return {"mensagem": "Tarefa deletada com sucesso"}
