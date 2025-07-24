from stockManagerApi.Contrib.models import BaseModel
from sqlalchemy import Integer, String, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

class StockMovement(BaseModel):
    __tablename__ = 'stock_movements'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey('products.pk_id'))
    product: Mapped['ProductModel'] = relationship(back_populates='products')
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    type: Mapped[str] = mapped_column(String(10), CheckConstraint("type IN ('in', 'out')"),nullable=False)
    date_movement: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    
    