from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

from base_database.models.user_shame import UserBase, UserTable

DATABASE_URL: str = "postgresql+psycopg2://postgres:postgres@localhost:5432/users_db"

engine = create_engine(
    DATABASE_URL,
    pool_size=20,
    max_overflow=10,
    pool_pre_ping=True,
    pool_recycle=3600,
    echo=False
)

def create_db_and_tables() -> None:
    UserBase.metadata.create_all(engine)

create_db_and_tables()