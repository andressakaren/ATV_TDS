from fastapi import FastAPI
from .database import Base, engine
from . import auth, tasks

# Cria as tabelas automaticamente se não existirem
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Inclui os arquivos de rotas
app.include_router(auth.router)
app.include_router(tasks.router)
