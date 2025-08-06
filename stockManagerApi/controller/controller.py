from sqlalchemy.orm import Session
from models import models
from schemas import schemas
from sqlalchemy import func, case
import datetime

# Category
def get_categories(db: Session):
    return db.query(models.CategoryModel).all()

def create_category(db: Session, data: schemas.Category):
    obj = models.Category(name=data.name)
    db.add(obj); db.commit(); db.refresh(obj)
    return obj

# Products
def get_products(db: Session):
    return db.query(models.ProductModel).all()

def create_product(db: Session, data: schemas.Product, category_id: int):
    obj = models.ProductModel(
        name=data.name,
        code=data.code,
        preco=data.preco,
        create_at=data.create_at or datetime.utcnow(),
        id_category=category_id
    )
    db.add(obj); db.commit(); db.refresh(obj)
    return obj

# Movement
def create_movement(db: Session, data: schemas.StockMovement):
    obj = models.StockMovement(**data.model_dump())
    db.add(obj); db.commit(); db.refresh(obj)
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
