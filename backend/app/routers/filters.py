from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/filters", tags=["Filters"])


@router.post("/", response_model=schemas.FilterRead)
def create_filter(filter_data: schemas.FilterCreate, db: Session = Depends(get_db)):
    db_filter = models.Filter(**filter_data.model_dump())
    db.add(db_filter)
    db.commit()
    db.refresh(db_filter)
    return db_filter


@router.get("/{filter_id}", response_model=schemas.FilterRead)
def get_filter(filter_id: int, db: Session = Depends(get_db)):
    filter_obj = db.query(models.Filter).filter(models.Filter.id == filter_id).first()
    if not filter_obj:
        raise HTTPException(status_code=404, detail="Filter not found")
    return filter_obj


@router.get("/", response_model=list[schemas.FilterRead])
def list_filters(db: Session = Depends(get_db)):
    return db.query(models.Filter).all()


@router.patch("/{filter_id}", response_model=schemas.FilterRead)
def update_filter(filter_id: int, update_data: schemas.FilterUpdate, db: Session = Depends(get_db)):
    filter_obj = db.query(models.Filter).filter(models.Filter.id == filter_id).first()
    if not filter_obj:
        raise HTTPException(status_code=404, detail="Filter not found")

    for field, value in update_data.model_dump(exclude_unset=True).items():
        setattr(filter_obj, field, value)

    db.commit()
    db.refresh(filter_obj)
    return filter_obj


@router.delete("/{filter_id}")
def delete_filter(filter_id: int, db: Session = Depends(get_db)):
    filter_obj = db.query(models.Filter).filter(models.Filter.id == filter_id).first()
    if not filter_obj:
        raise HTTPException(status_code=404, detail="Filter not found")

    db.delete(filter_obj)
    db.commit()
    return {"message": "Filter deleted successfully"}
