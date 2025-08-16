from pydantic import BaseModel
from typing import Optional, List

class ParcelBase(BaseModel):
    address: str
    owner: Optional[str] = None

class ParcelCreate(ParcelBase):
    pass

class ParcelUpdate(BaseModel):
    address: Optional[str] = None
    owner: Optional[str] = None

class ParcelRead(ParcelBase):
    id: int

    class Config:
        from_attributes = True

class ParcelList(BaseModel):
    parcels: List[ParcelRead]
    total: int
