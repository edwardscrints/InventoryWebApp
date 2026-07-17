### clase de estructura de tabla de productos y su historial
### Mapea tablas de productos y su historial para persistencia de datos
### Created By. Ing. Edward Gabriel Acosta

from sqlalchemy import Column, Integer, String, Text, Numeric, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database.config import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String(50), unique=True, index=True, nullable=False)
    nombre = Column(String(100), nullable=False)
    categoria = Column(String(50), nullable=False)
    presentacion = Column(String(20), nullable=False)
    descripcion = Column(Text, nullable=True)
    precio = Column(Numeric(10, 2), nullable=False)
    stock = Column(Integer, nullable=False)
    estado = Column(String(20), default="Activo", nullable=False)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    # Relación uno a muchos con el historial
    historial = relationship("ProductHistory", back_populates="producto", cascade="all, delete-orphan")


class ProductHistory(Base):
    __tablename__ = "product_history"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    action = Column(String(20), nullable=False)
    description = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relación inversa
    producto = relationship("Product", back_populates="historial")