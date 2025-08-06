from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from controller import controller
from schemas import schemas
import database


router = APIRouter(prefix="/categories", tags=["categories"])

def get_db():
    db = database.sessionlocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", status_code=status.HTTP_200_OK,response_model=list[schemas.CategoryOut])
def read_categories(db: Session = Depends(get_db)):
    return controller.get_categories(db)

@router.post("/", response_model=schemas.CategoryOut, status_code=status.HTTP_201_CREATED)
def create_category(cat: schemas.Category, db: Session = Depends(get_db)):
    return controller.create_category(db, cat)
