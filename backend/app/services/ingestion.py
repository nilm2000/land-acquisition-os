"""
Handles importing and cleaning parcel/project/filter data
from CSV, Excel, or other sources.
"""
import pandas as pd
from sqlalchemy.orm import Session
from app import models


def import_parcels_from_csv(file_path: str, db: Session):
    df = pd.read_csv(file_path)
    for _, row in df.iterrows():
        parcel = models.Parcel(
            apn=row.get("apn"),
            address=row.get("address"),
            city=row.get("city"),
            state=row.get("state"),
            zip_code=row.get("zip_code"),
            acreage=row.get("acreage"),
            owner=row.get("owner"),
            status=row.get("status"),
        )
        db.add(parcel)
    db.commit()
    return {"message": f"Imported {len(df)} parcels from {file_path}"}
