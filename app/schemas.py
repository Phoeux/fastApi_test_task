from pydantic import BaseModel


class AddressResponse(BaseModel):
    address: str | None = None

    class Config:
        orm_mode = True


class Data(AddressResponse):
    phone_number: str
