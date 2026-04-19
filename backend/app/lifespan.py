from contextlib import asynccontextmanager
from fastapi import FastAPI
from db.database import init_db

@asynccontextmanager
async def lifespan(_app: FastAPI):
    init_db(create_tables=True)
    yield
