from datetime import datetime
from pydantic import BaseModel, PositiveInt,Field
from typing import Annotated, Optional

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
    preco: Annotated[float, Field(gt=0, description="Product price")]

class ProductCreate(ProductBase):
    create_at: datetime = Field(default_factory=datetime.now)

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

class StockMovementBase(BaseModel):
    product_id: Annotated[int, Field(gt=0, description="Product ID")]
    quantity: Annotated[int, Field(description="Product Quantity", example=2)]
    type: Annotated[str, Field(description="Movement Type", pattern="^(in|out)$")]
    date_movement: datetime

class StockMovementCreate(StockMovementBase):
    date_movement: datetime = Field(default_factory=datetime.now)

class StockMovementUpdate(BaseModel):
    quantity: Optional[int] = Field(None, description="Product Quantity", example=2)
    type: Optional[str] = Field(None, description="Movement Type", pattern="^(in|out)$")
    date_movement: Optional[datetime] = None

    class Config:
        from_attributes = True

class StockMovement(StockMovementBase):
    id: int
    uuid: str

    class Config:
        from_attributes = True

class StockMovementOut(StockMovement):
    pk_id: int

class StockReport(BaseModel):
    product_id: int
    total_entries: int
    total_exits: int
    current_stock: int

    class Config:
        from_attributes = True
