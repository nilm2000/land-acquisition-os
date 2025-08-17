from pydantic import BaseModel

class ParcelBase(BaseModel):
    address: str
    owner_name: str | None = None
    parcel_id: str

class ParcelCreate(ParcelBase):
    pass

class ParcelRead(ParcelBase):
    id: int
    class Config:
        from_attributes = True
