from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

# Configurações
SECRET_KEY = "segredo_super_secreto"  # Pode mudar depois
ALGORITHM = "HS256"
TOKEN_EXPIRA_MINUTOS = 30

# Criptografia de senhas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def gerar_hash(senha: str) -> str:
    return pwd_context.hash(senha)

def verificar_senha(senha: str, senha_hash: str) -> bool:
    return pwd_context.verify(senha, senha_hash)

def criar_token(dados: dict):
    dados_copia = dados.copy()
    expira = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRA_MINUTOS)
    dados_copia.update({"exp": expira})
    return jwt.encode(dados_copia, SECRET_KEY, algorithm=ALGORITHM)
