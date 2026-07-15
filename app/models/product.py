from sqlalchemy import Column, Integer, String, Float
from db.base import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    price = Column(Float)
    description = Column(String(255))
    image_url = Column(String(500), nullable=True)

