import uvicorn
from fastapi import FastAPI, Depends, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from crud.product import get_products
from db.session import engine
from db.base import Base
from api import auth, product, order
from sqlalchemy.orm import Session
from db.session import get_db
from api.deps import get_current_user

from fastapi.templating import Jinja2Templates 
from fastapi.staticfiles import StaticFiles

# This creates tables in MySQL
Base.metadata.create_all(engine)

app = FastAPI()

# Setup Templates
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(auth.router)
app.include_router(product.router)
app.include_router(order.router)

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return RedirectResponse(url="/login")

@app.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse(request=request, name="login.html", context={"request": request})

@app.get("/register", response_class=HTMLResponse)
def register_page(request: Request):
    return templates.TemplateResponse(request=request, name="register.html", context={"request": request})

@app.get("/products-page", response_class=HTMLResponse)
def products_page(request: Request, db: Session = Depends(get_db)):
    print("iuw8yewdygu8ewgbdchiu9ufefiodui2ie")
    try:
        user = get_current_user(request, db)
        print(user,'yrdfgjewqasgjkliuyt')
        products = get_products(db)
        print(products,'iuytrdshjkl;mnbvcxzawertyu')
        return templates.TemplateResponse(
            request=request,
            name="products.html",
            context={"request": request, "products": products, "user": user}
        )
    except:
        return RedirectResponse(url="/login")

@app.get("/add-product-page", response_class=HTMLResponse)
def add_product_page(request: Request, db: Session = Depends(get_db)):
    user = get_current_user(request, db)

    if user.role != "admin":
        return RedirectResponse(url="/products-page")
    return templates.TemplateResponse(
        request=request,
        name="add_product.html",
        context={"request": request, "user": user}
    )

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="127.0.0.1", port=8009, reload=False)