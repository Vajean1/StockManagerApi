from pydantic import BaseModel, Field, PositiveFloat, PositiveInt
from typing import Annotated
from datetime import datetime

class BaseSchema(BaseModel):
    class Config:
        extra = "forbid"
        from_attributes = True

class Category(BaseSchema):
    name: Annotated[str, Field(description="Category Name", example="Eletronics", max_length=100)]

class CategoryOut(Category):
    pk_id: PositiveInt

class Product(BaseSchema):
    name: Annotated[str, Field(description="Product Name", example="LapTop", max_length=100)]
    code: Annotated[str, Field(description="Product Description", example="LAP123", max_length=50)]
    preco: PositiveFloat

class ProductOut(Product):
    pk_id: int
    create_at: Annotated[datetime, Field(description="Create Date", example="01/01/2001")]
    category: CategoryOut

class StockMovement(BaseSchema):
    product_id: int
    quantity: int
    type: str = Field(..., regex="^(in|out)$")
    date_movement: datetime

class StockMovementOut(StockMovement):
    pk_id: int
    product: ProductOut

class StockReport(BaseSchema):
    product_id: int
    current_stock: int
    total_entries: int
    total_exits: int
