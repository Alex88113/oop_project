from decimal import Decimal

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base_database.models.book_shame import BookBase, BookDB

DATABASE_URL: str = 'postgresql+psycopg2://postgres:postgres@localhost:5432/book_db'

engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(engine)

def create_tables() -> None:
    BookBase.metadata.create_all(engine)

def insert_data() -> None:
    with Session() as session:
        book1 = BookDB(
            title='Clean code',
            author='Robert Martin',
            year=2008,
            price=Decimal(2500.0)
            )
        session.add_all([book1])
        session.commit()
        
if __name__ == "__main__":
    create_tables()
    insert_data()
