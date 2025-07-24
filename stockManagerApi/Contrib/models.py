from sqlalchemy import UUID
from uuid import uuid4
from sqlalchemy.dialects.sqlite import UUID as SQLiteUUID
from sqlalchemy.orm import DeclarativeBase, Mapped, MappedColumn

class BaseModel(DeclarativeBase):
    id: Mapped[UUID] = MappedColumn(SQLiteUUID(as_uuid=True), default=uuid4, nullable=False)