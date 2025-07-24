from stockManagerApi.Contrib.models import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Float, DateTime

class ProductModel(BaseModel):
    __tablename__ = 'products'
    
    pk_id: Mapped[int] = mapped_column(Integer,primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    code: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    preco: Mapped[float] = mapped_column(Float, nullable=False)
    create_at: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    category: Mapped['Category'] = relationship (back_populates='categories')
    id_category: Mapped[int] = mapped_column(Integer, foreign_key='categories.pk_id')
