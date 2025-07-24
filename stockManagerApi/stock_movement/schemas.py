from stockManagerApi.Contrib.schemas import BaseSchema
from pydantic import Field
from typing import Annotated

class StockMovement(BaseSchema):
    quantity: Annotated[int, Field(description="Quantity of stock movement", example=10)]
    type: Annotated[str, Field(description="Type of stock movement", example="IN", max_length=10)]