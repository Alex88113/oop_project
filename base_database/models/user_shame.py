from datetime import datetime

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import (
DeclarativeBase,
Mapped,
mapped_column,
relationship
)
from sqlalchemy import String

class UserBase(DeclarativeBase):
    pass

class UserTable(UserBase):
    __tablename__: str = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    age: Mapped[int] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    def __repr__(self) -> str:
        return f'UserTable(id={self.id}, username={self.username}, email={self.email})'

