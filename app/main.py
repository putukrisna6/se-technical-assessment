from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.session import engine
from app.db.base import Base
from app.api import feedbacks


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["POST", "PUT", "PATCH", "GET", "DELETE", "HEAD", "OPTIONS"],
    allow_headers=["Origin", "Content-Length", "Content-Type", "Authorization"],
)


@app.on_event("startup")
async def startup_event():
    await create_db_and_tables()

app.include_router(feedbacks.router)
