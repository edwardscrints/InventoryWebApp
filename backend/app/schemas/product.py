### clases de validaciones estrcitas de logica de negocio
### Retorna un error HTTP 422 automático en datos incorrectos
### Created By. Ing. Edward Gabriel Acosta

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ProductBase(BaseModel):
    sku: str = Field(..., max_length=50, description="Código único de producto (SKU)")
    nombre: str = Field(..., max_length=100, description="Nombre del producto, máximo 100 caracteres")
    categoria: str = Field(..., max_length=50, description="Categoría (Ej: Cuidado de cabello, Piel)")
    presentacion: str = Field(..., max_length=20, description="Presentación (Ej: 200gr, 500ml)")
    descripción: Optional[str] = None
    precio: float = Field(..., gt=0, description="El precio debe ser mayor que 0")
    stock: int = Field(..., ge=0, description="El stock debe ser mayor o igual a 0")
    estado: str = Field(default="Activo", pattern="^(Activo|Inactivo)$")

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    sku: Optional[str] = Field(None, max_length=50)
    nombre: Optional[str] = Field(None, max_length=100)
    categoria: Optional[str] = Field(None, max_length=50)
    presentacion: Optional[str] = Field(None, max_length=20)
    descripción: Optional[str] = None
    precio: Optional[float] = Field(None, gt=0)
    stock: Optional[int] = Field(None, ge=0)
    estado: Optional[str] = Field(None, pattern="^(Activo|Inactivo)$")

class ProductResponse(ProductBase):
    id: int
    fecha_creación: datetime

    class Config:
        from_attributes = True 

class ProductHistoryResponse(BaseModel):
    id: int
    product_id: int
    action: str
    description: str
    created_at: datetime

    class Config:
        from_attributes = True