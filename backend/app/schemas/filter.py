from pydantic import BaseModel
from typing import Optional, Dict, Any

class FilterBase(BaseModel):
    name: str
    criteria: Dict[str, Any]

class FilterCreate(FilterBase):
    pass

class FilterUpdate(BaseModel):
    name: Optional[str] = None
    criteria: Optional[Dict[str, Any]] = None

class FilterRead(FilterBase):
    id: int

    class Config:
        from_attributes = True
