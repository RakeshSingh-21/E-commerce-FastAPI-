from sqlalchemy.orm import Session
from models.order import Order

def create_order(db: Session, order):
    db_order = Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order