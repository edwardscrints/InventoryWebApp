### clase principal de FastAPI para Backend
### Arranque de API RESTful, se incluye el inicializador de BD, router de productose impresion estructurada de Logs en Consola
### Created By. Ing. Edward Gabriel Acosta

import logging
from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database.init_db import init_database
from fastapi.middleware.cors import CORSMiddleware
from app.routers import product

# Configuración del Logger (estilo printf estructurado)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Iniciando servidor... Verificando base de datos.")
    init_database()
    logger.info("Servidor listo para recibir peticiones.")
    yield
    logger.info("Apagando servidor de AssisPrex...")

app = FastAPI(title="API CRUD AssisPrex", lifespan=lifespan)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Conectando los endpoints de productos
app.include_router(product.router, prefix="/products", tags=["Products"])