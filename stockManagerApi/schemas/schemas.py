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
    pk_id: PositiveInt
    create_at: Annotated[datetime, Field(description="Create Date", example="01/01/2001")]
    category: CategoryOut

class StockMovement(BaseSchema):
    product_id: PositiveInt
    quantity: Annotated[int, Field(description="Product Quantity", example=2)]
    type: Annotated[str, Field(description="Produuct Type", pattern="^(in|out)$")]
    date_movement: Annotated[datetime, Field(description="Movement date")]

class StockMovementOut(StockMovement):
    pk_id: int
    product: ProductOut

class StockReport(BaseSchema):
    product_id: int
    current_stock: Annotated[int, Field(description="Current Stock")]
    total_entries: Annotated[int, Field(description="Total entries")]
    total_exits: Annotated[int, Field(description="Total entries")]
