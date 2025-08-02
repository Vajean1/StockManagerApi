from pydantic import BaseModel, Field, PositiveFloat
from typing import List, Optional
from datetime import datetime

class Config:
    orm_mode = True

class Category(BaseModel):
    name: str = Field(..., max_length=100)

class CategoryOut(Category):
    pk_id: int

class Product(BaseModel):
    name: str = Field(..., max_length=100)
    code: str = Field(..., max_length=50)
    preco: PositiveFloat

class ProductOut(Product):
    pk_id: int
    create_at: datetime
    category: CategoryOut

class StockMovement(BaseModel):
    product_id: int
    quantity: int
    type: str = Field(..., regex="^(in|out)$")
    date_movement: datetime

class StockMovementOut(StockMovement):
    pk_id: int
    product: ProductOut

class StockReport(BaseModel):
    product_id: int
    current_stock: int
    total_entries: int
    total_exits: int
