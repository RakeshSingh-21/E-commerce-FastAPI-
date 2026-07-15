# from pydantic import BaseModel


# class ProductCreate(BaseModel):
#     name: str
#     price: float
#     description: str

# class ProductUpdate(BaseModel):
#     name: str | None = None
#     description: str | None = None
#     price: float | None = None


from pydantic import BaseModel
from typing import Optional

class ProductCreate(BaseModel):
    name: str
    price: float
    description: str
    image_url: Optional[str] = None

class ProductUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    image_url: str | None = None