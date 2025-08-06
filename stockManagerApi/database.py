from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import BaseModel

SQLITE_DATABASE_URL = "sqlite:///./stock_manager.db"

engine = create_engine(SQLITE_DATABASE_URL, connect_args={"check_same_thread": False})
sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    BaseModel.metadata.create_all(bind=engine)
