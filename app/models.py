from sqlalchemy import Column, Integer, String

from app.database import Base


class Data(Base):
    __tablename__ = 'data'

    id = Column(Integer, primary_key=True, index=True)
    phone_number = Column(String, unique=True)
    address = Column(String, unique=True)
