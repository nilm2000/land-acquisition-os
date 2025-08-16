# app/main.py
from fastapi import FastAPI
from app.database import Base, engine
from app.routers import parcels, users, auth

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(parcels.router)
app.include_router(users.router)
app.include_router(auth.router)
