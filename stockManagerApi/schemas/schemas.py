from pydantic import BaseModel, Field, PositiveFloat, PositiveInt
from typing import Annotated, Optional
from datetime import datetime

class BaseSchema(BaseModel):
    class Config:
        extra = "forbid"
        from_attributes = True

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int
    uuid: str

    class Config:
        from_attributes = True

class CategoryOut(Category):
    pk_id: PositiveInt

class ProductBase(BaseModel):
    name: str
    code: str
    preco: float
    create_at: Optional[datetime] = None

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    uuid: str
    category_id: int

    class Config:
        from_attributes = True

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
