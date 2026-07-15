from fastapi import APIRouter, Depends, HTTPException, Response, Form
from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserLogin
from crud.user import create_user, get_user_by_email
from core.security import verify_password, create_access_token
from db.session import get_db
from fastapi.responses import RedirectResponse

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
def register_user(
    name: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    role: str = Form("user"),
    db: Session = Depends(get_db)
):
    user = UserCreate(name=name, email=email, password=password, role=role)
    create_user(db, user)
    return RedirectResponse(url="/login", status_code=303)

@router.post("/login")
def login(
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    db_user = get_user_by_email(db, email)
    if not db_user or not verify_password(password, db_user.password):
        raise HTTPException(status_code=400, detail="Incorrect credentials")
    
    token = create_access_token({
        "sub": db_user.email,
        "role": db_user.role,
        "name": db_user.name
    })
    
    response = RedirectResponse(url="/products-page", status_code=303)
    response.set_cookie(key="access_token", value=token, httponly=True)
    return response

@router.post("/logout")
def logout():
    response = RedirectResponse(url="/login", status_code=303)
    response.delete_cookie("access_token")
    return response