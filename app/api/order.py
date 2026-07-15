from fastapi import APIRouter, Depends, Form, Request
from sqlalchemy.orm import Session
from schemas.order import OrderCreate
from crud.order import create_order
from db.session import get_db
from api.deps import get_current_user
from fastapi.responses import RedirectResponse

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/")
def place_order(
    product_id: int = Form(...),
    request: Request = None,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    order = OrderCreate(user_id=user.id, product_id=product_id)
    create_order(db, order)
    return RedirectResponse(url="/products-page", status_code=303)