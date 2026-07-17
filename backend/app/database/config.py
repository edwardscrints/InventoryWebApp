### Clase de Conexión a sistema de Persistencia
### retorna sesion de BD para manejo transaccional
### Created By. Ing. Edward Gabriel Acosta

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://usuario:password@localhost:5432/assisprex_db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

## Inyección de dependencias para FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()