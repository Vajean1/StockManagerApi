from stockManagerApi.Contrib.schemas import BaseSchema
from pydantic import Field
from typing import Annotated

class Category(BaseSchema):
    name: Annotated[str, Field(description="Category Name", example="Electronics", max_length=100)]