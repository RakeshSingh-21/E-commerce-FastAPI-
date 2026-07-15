# from sqlalchemy.orm import Session
# from models.product import Product

# def create_product(db: Session, product):
#     db_product = Product( 
#         name=product["name"],
#         price=product["price"],
#         description=product["description"]
#     )
#     db.add(db_product)
#     db.commit()
#     db.refresh(db_product)
#     return db_product


# # List all products
# def get_products(db: Session):
#     return db.query(Product).all()

# # Get single product by Id
# def get_product_by_id(db: Session, product_id: int):
#     return db.query(Product).filter(Product.id == product_id).first()

# def update_product(db: Session, product_id: int, product_data):
#     product = get_product_by_id(db, product_id)

#     if not product:
#         return None
#     product.name = product_data.name
#     product.description = product_data.description
#     product.price = product_data.price
#     db.commit()
#     db.refresh(product)
#     return product


# def delete_product(db: Session, product_id: int):
#     product = get_product_by_id(db, product_id)

#     if not product:
#         return None
#     db.delete(product)
#     db.commit()
#     return product


from sqlalchemy.orm import Session
from models.product import Product

def create_product(db: Session, product):
    db_product = Product( 
        name=product["name"],
        price=product["price"],
        description=product["description"],
        image_url=product.get("image_url")  # Add this line
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# List all products
def get_products(db: Session):
    return db.query(Product).all()

# Get single product by Id
def get_product_by_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def update_product(db: Session, product_id: int, product_data):
    product = get_product_by_id(db, product_id)

    if not product:
        return None
    product.name = product_data.name
    product.description = product_data.description
    product.price = product_data.price
    if product_data.image_url:
        product.image_url = product_data.image_url
    db.commit()
    db.refresh(product)
    return product

def delete_product(db: Session, product_id: int):
    product = get_product_by_id(db, product_id)

    if not product:
        return None
    db.delete(product)
    db.commit()
    return product