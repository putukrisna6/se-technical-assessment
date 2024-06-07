from fastapi import FastAPI
from app.db.session import engine
from app.db.base import Base
from app.api import feedbacks


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    await create_db_and_tables()

app.include_router(feedbacks.router)
