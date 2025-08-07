from sqlalchemy.orm import Session
from models import models
from schemas import schemas
from sqlalchemy import func, case, select
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
import datetime

# Category
def get_categories(db: Session):
    return db.query(models.CategoryModel).all()

def create_category(db: Session, data: schemas.Category):
    try:
        obj = models.CategoryModel(
            name=data.name,
            pk_id=0  # Initialize with 0
        )
        db.add(obj)
        db.commit()
        obj.pk_id = obj.id  # Set pk_id to match id after commit
        db.commit()
        db.refresh(obj)
        return obj
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail=f"Category with name '{data.name}' already exists"
        )

def get_category_by_id(db: Session, category_id: int):
    return db.query(models.CategoryModel).filter(
        models.CategoryModel.id == category_id
    ).first()

# Products
def get_products(db: Session):
    return db.query(models.ProductModel).all()

def create_product(db: Session, data: schemas.ProductCreate, category_id: int):
    try:
        obj = models.ProductModel(
            name=data.name,
            code=data.code,
            preco=data.preco,
            create_at=data.create_at,
            category_id=category_id,
            pk_id=0  # Initialize with 0
        )
        db.add(obj)
        db.commit()
        obj.pk_id = obj.id  # Set pk_id to match id after commit
        db.commit()
        db.refresh(obj)
        return obj
    except IntegrityError as e:
        db.rollback()
        if "UNIQUE constraint failed: products.code" in str(e):
            raise HTTPException(
                status_code=400,
                detail=f"Product with code '{data.code}' already exists"
            )
        raise HTTPException(
            status_code=400,
            detail="Database integrity error"
        )

def get_product_by_id(db: Session, product_id: int):
    return db.query(models.ProductModel).filter(models.ProductModel.id == product_id).first()

# Movement
def create_stock_movement(db: Session, data: schemas.StockMovementCreate):
    obj = models.StockMovement(
        product_id=data.product_id,
        quantity=data.quantity,
        type=data.type,
        date_movement=data.date_movement,
        pk_id=0  # Initialize with 0
    )
    db.add(obj)
    db.commit()
    obj.pk_id = obj.id  # Set pk_id to match id after commit
    db.commit()
    db.refresh(obj)
    return obj

def get_stock_report(db: Session):
    subq = (
        db.query(
            models.StockMovement.product_id,
            func.sum(case([(models.StockMovement.type=='in', models.StockMovement.quantity)], else_=0)).label("total_entries"),
            func.sum(case([(models.StockMovement.type=='out', models.StockMovement.quantity)], else_=0)).label("total_exits"),
        )
        .group_by(models.StockMovement.product_id)
        .subquery()
    )
    return (
        db.query(
            models.ProductModel.pk_id.label("product_id"),
            (subq.c.total_entries - subq.c.total_exits).label("current_stock"),
            subq.c.total_entries,
            subq.c.total_exits,
        )
        .join(subq, subq.c.product_id==models.ProductModel.pk_id)
        .all()
    )

def get_stock_report_by_product(db: Session, product_id: int):
    movements = db.query(
        models.StockMovement.product_id,
        func.sum(
            case(
                (models.StockMovement.type == 'in', models.StockMovement.quantity),
                else_=0
            )
        ).label('total_entries'),  # Changed from total_in
        func.sum(
            case(
                (models.StockMovement.type == 'out', models.StockMovement.quantity),
                else_=0
            )
        ).label('total_exits')     # Changed from total_out
    ).filter(
        models.StockMovement.product_id == product_id
    ).group_by(
        models.StockMovement.product_id
    ).first()

    if not movements:
        return None

    return {
        "product_id": product_id,
        "total_entries": movements.total_entries or 0,  # Changed field name
        "total_exits": movements.total_exits or 0,      # Changed field name
        "current_stock": (movements.total_entries or 0) - (movements.total_exits or 0)
    }

def list_stock_movements(db: Session, skip: int = 0, limit: int = 100):
    """
    List stock movements with pagination
    """
    return db.query(models.StockMovement)\
        .offset(skip)\
        .limit(limit)\
        .all()

def update_movement(db: Session, movement_id: int, data: schemas.StockMovementUpdate):
    movement = db.query(models.StockMovement).filter(
        models.StockMovement.id == movement_id
    ).first()
    
    if not movement:
        raise HTTPException(status_code=404, detail="Stock movement not found")
    
    if data.quantity is not None:
        movement.quantity = data.quantity
    if data.type is not None:
        movement.type = data.type
    if data.date_movement is not None:
        movement.date_movement = data.date_movement
    
    db.commit()
    db.refresh(movement)
    return movement

def get_stock_movement(db: Session, movement_id: int):
    return db.query(models.StockMovement).filter(
        models.StockMovement.id == movement_id
    ).first()

def delete_stock_movement(db: Session, movement_id: int):
    """
    Delete a stock movement by ID
    """
    movement = db.query(models.StockMovement).filter(
        models.StockMovement.id == movement_id
    ).first()
    
    if not movement:
        raise HTTPException(status_code=404, detail="Stock movement not found")
    
    db.delete(movement)
    db.commit()
    return {"message": "Stock movement deleted successfully"}

