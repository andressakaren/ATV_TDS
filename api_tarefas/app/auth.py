from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app import database, models, utils

from pydantic import BaseModel

router = APIRouter(prefix="/auth")

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

class UsuarioCriar(BaseModel):
    username: str
    email: str
    password: str

class UsuarioLogin(BaseModel):
    username: str
    password: str

@router.post("/signup")
def cadastrar_usuario(dados: UsuarioCriar, db: Session = Depends(get_db)):
    if db.query(models.Usuario).filter_by(username=dados.username).first():
        raise HTTPException(status_code=400, detail="Usuário já existe")

    senha_hash = utils.gerar_hash(dados.password)
    novo = models.Usuario(username=dados.username, email=dados.email, password_hash=senha_hash)
    db.add(novo)
    db.commit()
    return {"mensagem": "Usuário cadastrado com sucesso!"}

@router.post("/login")
def login(dados: UsuarioLogin, db: Session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter_by(username=dados.username).first()

    if not usuario or not utils.verificar_senha(dados.password, usuario.password_hash):
        raise HTTPException(status_code=401, detail="Usuário ou senha inválidos")

    token = utils.criar_token({"sub": str(usuario.id)})
    return {"access_token": token, "token_type": "bearer"}
