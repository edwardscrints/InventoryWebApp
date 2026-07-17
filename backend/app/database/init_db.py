### Clase de creación de estructura de Base de Datos
### ejecuta script.sql para creacion de Estructura
### Created By. Ing. Edward Gabriel Acosta

import os
from sqlalchemy import text
from app.database.config import engine, Base
from app.models.product import Product, ProductHistory

def init_database():
    """Crea las tablas en la base de datos basándose en los modelos de SQLAlchemy."""
    print(f"Verificando y creando estructura de base de datos desde el ORM...")
    Base.metadata.create_all(bind=engine)
    print(f"Base de datos lista")