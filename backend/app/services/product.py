### clase de gestion de producto
### Implementa la lógica de negocio para productos
### Created By. Ing. Edward Gabriel Acosta

from sqlalchemy.orm import Session
from sqlalchemy import func
from fastapi import HTTPException
from app.models.product import Product, ProductHistory
from app.schemas.product import ProductCreate, ProductUpdate
from datetime import datetime

def _registrar_historial(db: Session, product_id: int, action: str, description: str):
    """Función de apoyo para registrar eventos en la bitácora."""
    historial = ProductHistory(
        product_id=product_id,
        action=action,
        description=description
    )
    db.add(historial)

def create_product(db: Session, product_data: ProductCreate):
    # Se agrego verificación que el SKU no exista
    existe_sku = db.query(Product).filter(Product.sku == product_data.sku).first()
    if existe_sku:
        raise HTTPException(status_code=400, detail="El SKU ya está registrado.")

    db_product = Product(**product_data.model_dump())
    db.add(db_product)
    db.flush()

    _registrar_historial(db, db_product.id, "CREATE", f"Producto '{db_product.nombre}' creado.")

    db.commit()
    db.refresh(db_product)
    return db_product

def get_products(db: Session, skip: int = 0, limit: int = 100, search: str = None):
    query = db.query(Product).filter(Product.deleted_at.is_(None))
    
    if search:
        query = query.filter(
            (Product.nombre.ilike(f"%{search}%")) | 
            (Product.sku.ilike(f"%{search}%"))
        )
        
    return query.offset(skip).limit(limit).all()

def get_product_by_id(db: Session, product_id: int):
    product = db.query(Product).filter(
        Product.id == product_id, 
        Product.deleted_at.is_(None)
    ).first()
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado.")
    return product

def update_product(db: Session, product_id: int, product_data: ProductUpdate):
    db_product = get_product_by_id(db, product_id)

    update_data = product_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_product, key, value)
    
    _registrar_historial(db, db_product.id, "UPDATE", "Se actualizaron los datos del producto.")
    
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = get_product_by_id(db, product_id)
    

    db_product.deleted_at = datetime.now()
    
    _registrar_historial(db, db_product.id, "DELETE", "Producto eliminado lógicamente (Soft Delete).")
    
    db.commit()
    return {"message": "Producto eliminado con éxito"}

def change_product_status(db: Session, product_id: int):
    db_product = get_product_by_id(db, product_id)
    
    # Cambio de estado
    nuevo_estado = "Inactivo" if db_product.estado == "Activo" else "Activo"
    db_product.estado = nuevo_estado
    
    _registrar_historial(db, db_product.id, "STATUS_CHANGE", f"Estado cambiado a {nuevo_estado}.")
    
    db.commit()
    db.refresh(db_product)
    return db_product