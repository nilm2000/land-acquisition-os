from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.parcel import Parcel
from app.schemas.parcel import ParcelCreate, ParcelRead
from app.utils import get_current_user
from typing import List

router = APIRouter(prefix="/parcels", tags=["parcels"])

@router.get("/", response_model=List[ParcelRead])
def list_parcels(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(Parcel).all()

@router.post("/", response_model=ParcelRead)
def create_parcel(parcel: ParcelCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    new_parcel = Parcel(**parcel.dict(), user_id=user.id)
    db.add(new_parcel)
    db.commit()
    db.refresh(new_parcel)
    return new_parcel
