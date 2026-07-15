# from fastapi import APIRouter, HTTPException, Depends, Form, Request
# from sqlalchemy.orm import Session
# from schemas.product import ProductCreate, ProductUpdate
# from crud.product import create_product, get_products, update_product, delete_product
# from db.session import get_db
# from api.deps import admin_required, get_current_user
# from fastapi.responses import RedirectResponse

# router = APIRouter(prefix="/products", tags=["Products"])

# @router.post("/")
# def add_product(
#         name: str = Form(...),
#         price: float = Form(...),
#         description: str = Form(...),
#         db: Session = Depends(get_db),
#         user = Depends(admin_required)
# ):
#     product_data = {
#         "name": name,
#         "price": price,
#         "description": description
#     }
#     create_product(db, product_data)
#     return RedirectResponse(url="/products-page", status_code=303)

# @router.get("/")
# def list_products(db: Session = Depends(get_db)):
#     return get_products(db)

# @router.post("/{product_id}/delete")
# def delete_product_api(
#     product_id: int,
#     db: Session = Depends(get_db),
#     user=Depends(admin_required)
# ):
#     deleted = delete_product(db, product_id)
#     if not deleted:
#         raise HTTPException(status_code=404, detail="Product not found")
#     return RedirectResponse(url="/products-page", status_code=303)

from fastapi import APIRouter, HTTPException, Depends, Form, File, UploadFile
from sqlalchemy.orm import Session
from schemas.product import ProductCreate, ProductUpdate
from crud.product import create_product, get_products, update_product, delete_product
from db.session import get_db
from api.deps import admin_required, get_current_user
from fastapi.responses import RedirectResponse
import shutil
import os
from pathlib import Path
import uuid

router = APIRouter(prefix="/products", tags=["Products"])

# Create uploads directory if it doesn't exist
UPLOAD_DIR = Path("static/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@router.post("/")
def add_product(
        name: str = Form(...),
        price: float = Form(...),
        description: str = Form(...),
        image: UploadFile = File(None),
        db: Session = Depends(get_db),
        user = Depends(admin_required)
):
    # Handle image upload
    image_url = None
    if image and image.filename:
        # Generate unique filename
        file_extension = Path(image.filename).suffix
        unique_filename = f"{uuid.uuid4().hex}{file_extension}"
        file_path = UPLOAD_DIR / unique_filename
        
        # Save the file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
        
        # Store relative URL path
        image_url = f"/static/uploads/{unique_filename}"
    
    product_data = {
        "name": name,
        "price": price,
        "description": description,
        "image_url": image_url
    }
    
    create_product(db, product_data)
    return RedirectResponse(url="/products-page", status_code=303)

@router.get("/")
def list_products(db: Session = Depends(get_db)):
    return get_products(db)

@router.post("/{product_id}/delete")
def delete_product_api(
    product_id: int,
    db: Session = Depends(get_db),
    user=Depends(admin_required)
):
    # Get product to delete its image
    product = delete_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    # Delete the image file if it exists
    if product.image_url:
        image_path = Path("static") / product.image_url.lstrip("/")
        if image_path.exists():
            image_path.unlink()
    
    return RedirectResponse(url="/products-page", status_code=303)