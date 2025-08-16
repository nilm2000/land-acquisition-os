# app/routers/parcels.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.parcel import Parcel
from app.schemas.parcel import ParcelCreate, ParcelRead
from app.utils.geospatial import point_in_polygon, to_geojson
import requests
from app.config import get_settings

router = APIRouter(prefix="/parcels", tags=["Parcels"])
settings = get_settings()

@router.post("/", response_model=ParcelRead)
def create_parcel(parcel: ParcelCreate, db: Session = Depends(get_db)):
    db_parcel = Parcel(**parcel.dict())
    db.add(db_parcel)
    db.commit()
    db.refresh(db_parcel)
    return db_parcel

@router.get("/{parcel_id}", response_model=ParcelRead)
def get_parcel(parcel_id: int, db: Session = Depends(get_db)):
    parcel = db.query(Parcel).filter(Parcel.id == parcel_id).first()
    if not parcel:
        raise HTTPException(status_code=404, detail="Parcel not found")
    return parcel

@router.get("/regrid/{lat}/{lon}")
def get_regrid_parcel(lat: float, lon: float):
    url = f"https://app.regrid.com/api/v1/parcels?lat={lat}&lon={lon}&token={settings.regrid_api_key}"
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Regrid API error")
    return response.json()
