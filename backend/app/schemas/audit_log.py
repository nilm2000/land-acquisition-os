from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AuditLogBase(BaseModel):
    action: str
    entity: str
    entity_id: int
    user_id: Optional[int] = None

class AuditLogCreate(AuditLogBase):
    pass

class AuditLogRead(AuditLogBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True
