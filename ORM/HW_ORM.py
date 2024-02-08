from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db', echo=True)


Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)


Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()


def create_product(name, price):
    product = Product(name=name, price=price)
    session.add(product)
    session.commit()
    print("Product created successfully.")

def read_products():
    products = session.query(Product).all()
    print("Products in the database:")
    for product in products:
        print(f"ID: {product.id}, Name: {product.name}, Price: {product.price}")

def update_product(product_id, new_name, new_price):
    product = session.query(Product).filter_by(id=product_id).first()
    if product:
        product.name = new_name
        product.price = new_price
        session.commit()
        print("Product updated successfully.")
    else:
        print("Product not found.")

def delete_product(product_id):
    product = session.query(Product).filter_by(id=product_id).first()
    if product:
        session.delete(product)
        session.commit()
        print("Product deleted successfully.")
    else:
        print("Product not found.")


create_product("Laptop", 1500)
create_product("Phone", 800)
read_products()
update_product(1, "Updated Laptop", 1800)
delete_product(2)
read_products()


session.close()
