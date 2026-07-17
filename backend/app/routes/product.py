### Endpoints de api
### Implementación de los métodos GET, POST, PUT, PATCH y DELETE para productos
### Created By. Ing. Edward Gabriel Acosta

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List

from app.database.config import get_db
from app.schemas.product import ProductCreate, ProductUpdate, ProductResponse
from app.services import product as product_service

import logging
logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/", response_model=ProductResponse, status_code=201)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    logger.info(f"Petición POST recibida para crear producto SKU: {product.sku}")
    return product_service.create_product(db=db, product_data=product)

@router.get("/", response_model=List[ProductResponse])
def get_products(
    skip: int = Query(0, description="Registros a omitir (Paginación)"),
    limit: int = Query(10, description="Límite de registros (Paginación)"),
    search: str = Query(None, description="Término de búsqueda (Nombre o SKU)"),
    db: Session = Depends(get_db)
):
    logger.info(f"Petición GET recibida. Búsqueda: {search}, Skip: {skip}, Limit: {limit}")
    return product_service.get_products(db=db, skip=skip, limit=limit, search=search)

@router.get("/{id}", response_model=ProductResponse)
def get_product(id: int, db: Session = Depends(get_db)):
    return product_service.get_product_by_id(db=db, product_id=id)

@router.put("/{id}", response_model=ProductResponse)
def update_product(id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    logger.info(f"Petición PUT recibida para actualizar producto ID: {id}")
    return product_service.update_product(db=db, product_id=id, product_data=product)

@router.patch("/{id}/status", response_model=ProductResponse)
def change_status(id: int, db: Session = Depends(get_db)):
    logger.info(f"Petición PATCH recibida para cambiar estado del producto ID: {id}")
    return product_service.change_product_status(db=db, product_id=id)

@router.delete("/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    logger.info(f"Petición DELETE recibida para eliminar lógicamente el producto ID: {id}")
    return product_service.delete_product(db=db, product_id=id)