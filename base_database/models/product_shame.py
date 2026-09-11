from sqlalchemy.orm import (
DeclarativeBase,
Mapped,
mapped_column
)
from sqlalchemy import String, Integer, Boolean


class ProductBase(DeclarativeBase):
    pass

class ProductTable(ProductBase):
    __tablename__: str = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    in_stock: Mapped[bool] = mapped_column(Boolean, default=True)