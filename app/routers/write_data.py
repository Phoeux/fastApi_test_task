from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.crud import create_data, update_data, partial_update
from app.database import SessionLocal, redis
from app.schemas import Data

router = APIRouter(
    prefix='/write_data',
    tags=['sql_write_data'],
    responses={404: {'description': 'Not found'}}
)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.post('/', status_code=status.HTTP_200_OK)
async def post_data(data: Data, db: Session = Depends(get_db)):
    sql_data = create_data(data, db)
    in_redis = redis.set(data.phone_number, data.address)
    return {'sql_data': sql_data, 'in_redis': in_redis}


@router.put('/', status_code=status.HTTP_200_OK)
async def put_data(data: Data, db: Session = Depends(get_db)):
    update_data(data, db)
    redis.set(data.phone_number, data.address)


@router.patch('/', status_code=status.HTTP_200_OK, response_model=Data)
async def patch_data(data_id: int, data: Data, db: Session = Depends(get_db)):
    return partial_update(data_id, data, db)
