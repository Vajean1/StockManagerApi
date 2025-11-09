from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from database import get_db
from schemas import schemas
from controller import controller
from typing import Annotated

# Routes for products

router = APIRouter(prefix="/products", tags=["products"])

@router.post("/", response_model=schemas.ProductOut)
def create_product(
    product: schemas.ProductCreate,
    category_id: Annotated[int, Query(gt=0)],
    db: Session = Depends(get_db)
):
    db_category = controller.get_category_by_id(db, category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return controller.create_product(db, product, category_id)

@router.get("/", response_model=list[schemas.Product])
def read_products(db: Session = Depends(get_db)):
    return controller.get_products(db)

@router.get("/{product_id}", response_model=schemas.Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = controller.get_product_by_id(db, product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product
