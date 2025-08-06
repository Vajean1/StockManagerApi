from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas import schemas
from controller import controller

router = APIRouter(prefix="/categories", tags=["categories"])

@router.post("/", response_model=schemas.Category)
def create_category(
    data: schemas.CategoryCreate,
    db: Session = Depends(get_db)
):
    return controller.create_category(db, data)

@router.get("/", response_model=list[schemas.Category])
def read_categories(db: Session = Depends(get_db)):
    return controller.get_categories(db)
