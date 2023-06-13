from fastapi import FastAPI

from app import models
from app.database import engine
from app.routers import check_data, write_data

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(check_data.router)
app.include_router(write_data.router)
