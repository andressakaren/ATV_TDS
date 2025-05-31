from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Caminho para o banco de dados SQLite
DATABASE_URL = "sqlite:///./tarefas.db"

# Cria o engine de conexão
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Gerenciador de sessões
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Classe base para os modelos
Base = declarative_base()
