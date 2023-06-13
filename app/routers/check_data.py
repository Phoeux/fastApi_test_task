from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud import get_address
from app.database import SessionLocal, redis

router = APIRouter(
    prefix='/check_data',
    tags=['sql_check_data'],
    responses={404: {'description': 'Not found'}}
)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.get("/")
async def check_data(phone: str, db: Session = Depends(get_db)):
    sql_phone_data = get_address(phone, db)
    redis_phone_data = redis.get(phone).decode('utf-8') if redis.get(phone) else None
    return redis_phone_data if sql_phone_data.first().address == redis_phone_data else 'Invalid phone number'
