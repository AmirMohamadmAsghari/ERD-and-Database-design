from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a SQLAlchemy engine to connect to the database
engine = create_engine('postgresql://username:password@localhost/my_database')

# Create a sessionmaker to interact with the database
Session = sessionmaker(bind=engine)

# Create a base class for declarative class definitions
Base = declarative_base()

# Define a class representing the products table
class Product(Base):
    __tablename__ = 'products'

    product_id = Column(Integer, primary_key=True)
    product_name = Column(String)
    category = Column(String)
    price = Column(Integer)
    quantity = Column(Integer)

# Method to read records from the products table
def read_products(session):
    products = session.query(Product).all()
    for product in products:
        print(product.product_name, product.category, product.price, product.quantity)

# Method to update a record in the products table
def update_product(session, product_id, new_quantity):
    product = session.query(Product).filter_by(product_id=product_id).first()
    if product:
        product.quantity = new_quantity
        session.commit()
        print(f"Updated quantity of {product.product_name} to {new_quantity}")
    else:
        print("Product not found")

# Method to delete a record from the products table
def delete_product(session, product_id):
    product = session.query(Product).filter_by(product_id=product_id).first()
    if product:
        session.delete(product)
        session.commit()
        print(f"Deleted product {product.product_name}")
    else:
        print("Product not found")

if __name__ == "__main__":
    # Create session
    session = Session()

    # Example usage: Read products
    print("Products in the database:")
    read_products(session)

    # Example usage: Update product quantity
    update_product(session, product_id=1, new_quantity=90)

    # Example usage: Delete a product
    delete_product(session, product_id=4)

    # Close session
    session.close()
