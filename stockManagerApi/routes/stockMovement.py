from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import schemas
from controller import controller
from typing import Optional

router = APIRouter(prefix="/stock-movements", tags=["stock-movements"])

@router.post("/", response_model=schemas.StockMovementOut)
def create_stock_movement(
    stock_movement: schemas.StockMovementCreate,
    db: Session = Depends(get_db)
):
    return controller.create_stock_movement(db=db, data=stock_movement)

@router.get("/{movement_id}", response_model=schemas.StockMovement)
def get_stock_report(movement_id: int, db: Session = Depends(get_db)):
    db_stock_movement = controller.get_stock_movement(db, movement_id=movement_id)
    if db_stock_movement is None:
        raise HTTPException(status_code=404, detail="Stock movement not found")
    return db_stock_movement

@router.get("/{product_id}/report", response_model=schemas.StockReport)
def get_stock_report_by_product(product_id: int, db: Session = Depends(get_db)):
    stock_report = controller.get_stock_report_by_product(db, product_id)
    if stock_report is None:
        raise HTTPException(status_code=404, detail="Stock report not found for this product")
    return stock_report

@router.get("/", response_model=list[schemas.StockMovement])
def list_stock_movements(
    skip: Optional[int] = 0,
    limit: Optional[int] = 100,
    db: Session = Depends(get_db)
):
    return controller.list_stock_movements(db=db, skip=skip, limit=limit)

@router.put("/{movement_id}", response_model=schemas.StockMovementOut)
def update_stock_movement(
    movement_id: int,
    stock_movement: schemas.StockMovementUpdate,
    db: Session = Depends(get_db)
):
    return controller.update_movement(db, movement_id, stock_movement)

@router.delete("/{movement_id}", status_code=200)
def delete_stock_movement(movement_id: int, db: Session = Depends(get_db)):
    return controller.delete_stock_movement(db=db, movement_id=movement_id)
