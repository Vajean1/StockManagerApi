from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import schemas
from controller import controller


#Routes for categories

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

@router.get("/{category_id}", response_model=schemas.Category)
def read_category(category_id: int, db: Session = Depends(get_db)):
    db_category = controller.get_category_by_id(db, category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category
