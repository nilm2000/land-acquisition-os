from fastapi import FastAPI
from app.database import Base, engine
from app.routers import auth, users, parcels

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(parcels.router)

@app.get("/")
def root():
    return {"message": "Land Acquisition OS API running 🚀"}
