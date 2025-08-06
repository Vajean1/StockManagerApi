from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

# Create SQLite database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./stock_manager.db"

# Create engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    from models.models import BaseModel
    BaseModel.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
