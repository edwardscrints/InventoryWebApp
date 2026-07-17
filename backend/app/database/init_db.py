### Clase de creación de estructura de Base de Datos
### ejecuta script.sql para creacion de Estructura
### Created By. Ing. Edward Gabriel Acosta

import os
from sqlalchemy import text
from app.database.config import engine

def init_database():
    """Ejecuta el script SQL inicial si las tablas no existen."""
    script_path = os.path.join(os.path.dirname(__file__), "../../../script.sql")
    
    with engine.connect() as connection:
        
        result = connection.execute(text("SELECT to_regclass('public.products');"))
        if result.scalar() is None:
            print("Tablas no encontradas. Ejecutando script.sql para automatizar creación...")
            try:
                with open(script_path, "r", encoding="utf-8") as file:
                    sql_script = file.read()
                    
                    connection.execute(text(sql_script))
                    connection.commit()
                print("Estructura de base de datos creada exitosamente.")
            except Exception as e:
                print(f"Error crítico al ejecutar script.sql: {e}")
        else:
            print("La base de datos ya cuenta con la estructura necesaria.")