from uuid import uuid4
from datetime import datetime
from sqlalchemy import Integer, String, Float, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class BaseModel(DeclarativeBase):
    __abstract__ = True
    uuid: Mapped[str] = mapped_column(String(36), default=lambda: str(uuid4()))

class CategoryModel(BaseModel):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    pk_id: Mapped[int] = mapped_column(Integer, nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)

    products: Mapped[list["ProductModel"]] = relationship(
        "ProductModel", back_populates="category"
    )

class ProductModel(BaseModel):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    pk_id: Mapped[int] = mapped_column(Integer)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    code: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    preco: Mapped[float] = mapped_column(Float, nullable=False)
    create_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))

    category: Mapped[CategoryModel] = relationship(
        "CategoryModel", back_populates="products"
    )
    stock_movements: Mapped[list["StockMovement"]] = relationship(
        "StockMovement", back_populates="product"
    )

class StockMovement(BaseModel):
    __tablename__ = 'stock_movements'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    pk_id: Mapped[int] = mapped_column(Integer, nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'))
    quantity: Mapped[int] = mapped_column(Integer)
    type: Mapped[str] = mapped_column(String(3)) 
    date_movement: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    product: Mapped["ProductModel"] = relationship("ProductModel", back_populates="stock_movements")
