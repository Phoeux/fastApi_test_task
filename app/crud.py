from fastapi import HTTPException
from sqlalchemy.orm import Session

from app import models
from app.schemas import Data


def get_address(phone_number: str, db: Session):
    return db.query(models.Data).filter(models.Data.phone_number == phone_number)


def create_data(data: Data, db: Session):
    db_data = models.Data(phone_number=data.phone_number, address=data.address)
    data_check = db.query(models.Data).filter(models.Data.phone_number == db_data.phone_number,
                                              models.Data.address == db_data.address).first()

    if data_check:
        raise HTTPException(status_code=400, detail="Item already exist")

    db.add(db_data)
    db.commit()
    db.refresh(db_data)

    return db_data


def update_data(new_data: Data, db: Session):
    data = db.query(models.Data).filter(models.Data.phone_number == new_data.phone_number).first()

    if data is None:
        raise HTTPException(status_code=404, detail="Item not found")

    data.phone_number = new_data.phone_number
    data.address = new_data.address

    db.add(data)
    db.commit()

    return data


def partial_update(data_id: int, data: Data, db: Session):
    new_data = data.dict(exclude_unset=True)
    old_data = db.query(models.Data).filter(models.Data.id == data_id)

    if old_data is None:
        raise HTTPException(status_code=404, detail="Item not found")

    old_data.update(new_data)
    db.commit()

    return old_data.first()
