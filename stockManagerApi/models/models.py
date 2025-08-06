from uuid import uuid4
from sqlalchemy import Integer, String, Float, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

#Base model for all models - Contains common fields and UUID generation
#UUID is a unique identifier for each record that is generated automatically and not visible to the user
# Recive a declarative base from SQLAlchemy that allows us to define models
class BaseModel(DeclarativeBase):
    id: Mapped[str] = mapped_column(
        String(36), default=lambda: str(uuid4()), primary_key=True)

class CategoryModel(BaseModel):
    __tablename__ = 'categories'

    pk_id: Mapped[int] = mapped_column(Integer, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)

    # Relationship to products
    products: Mapped[list["ProductModel"]] = relationship(
        "ProductModel", back_populates="category"
    )

class ProductModel(BaseModel):
    __tablename__ = 'products'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    code: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    preco: Mapped[float] = mapped_column(Float, nullable=False)
    create_at: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    id_category: Mapped[int] = mapped_column(ForeignKey('categories.pk_id'))

    category: Mapped[CategoryModel] = relationship(
        "CategoryModel", back_populates="products"
    )
    stock_movements: Mapped[list["StockMovement"]] = relationship(
        "StockMovement", back_populates="product"
    )

class StockMovement(BaseModel):
    __tablename__ = 'stock_movements'
    
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    product_id: Mapped[int] = mapped_column(ForeignKey('products.pk_id'))
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    type: Mapped[str] = mapped_column(
        String(10),
        CheckConstraint("type IN ('in', 'out')"),
        nullable=False
    )
    date_movement: Mapped[DateTime] = mapped_column(DateTime, nullable=False)

    product: Mapped[ProductModel] = relationship(
        "ProductModel", back_populates="stock_movements"
    )
