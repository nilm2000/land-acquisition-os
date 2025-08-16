# app/routers/projects.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.project import Project
from app.models.parcel import Parcel
from app.schemas.project import ProjectOut, ProjectDetail
from app.schemas.parcel import ParcelOut
from app.services.regrid import enrich_parcel

router = APIRouter(prefix="/projects", tags=["Projects"])


@router.get("/{project_id}", response_model=ProjectDetail)
def get_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    return project


@router.get("/{project_id}/parcels", response_model=List[ParcelOut])
def get_project_parcels(project_id: int, db: Session = Depends(get_db)):
    parcels = db.query(Parcel).filter(Parcel.project_id == project_id).all()
    if not parcels:
        raise HTTPException(status_code=404, detail="No parcels found for this project")

    enriched = [enrich_parcel(p) for p in parcels]
    return enriched
