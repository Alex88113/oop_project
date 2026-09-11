from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from base_database.models.product_shame import ProductBase, ProductTable

DB_URL: str = "postgresql+psycopg2://postgres:postgres@localhost:5432/products_db"
engine = create_engine(DB_URL, echo=False)


def create_db_and_tables() -> None:
    ProductBase.metadata.create_all(engine)


create_db_and_tables()

Session = sessionmaker(engine)


def insert_data(session: Session) -> None:
    product1 = ProductTable(name="Laptop asus x515", price=40.000, in_stock=True)
    product2 = ProductTable(name="Бандана", price=200, in_stock=True)
    product3 = ProductTable(name="Игровой коврик для мыши", price=1500, in_stock=False)

    session.add_all([product1, product2, product3])
    session.commit()


def print_all_products_db(session: Session) -> None:
    products = session.query(ProductTable).all()
    print('---------------- All data from products db ----------------')
    for product in products:
        print(f"ID: {product.id} | name: {product.name} | price: {product.price}")
    print('-----------------------------------------------------------')

def main() -> None:
    with Session() as session:
        insert_data(session)
        print_all_products_db(session)

main()