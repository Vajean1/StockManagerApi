from pydantic import Field, PositiveFloat
from typing import Annotated
from stockManagerApi.Contrib.schemas import BaseSchema

class Product(BaseSchema):
    name: Annotated[str, Field(description="Product Name", example="Laptop", max_length=100)]
    code: Annotated[str, Field(description="Product Code", example="LAP123", max_length=50)]
    preco: Annotated[PositiveFloat, Field(description="Product Price", example=999.99, ge=0)]