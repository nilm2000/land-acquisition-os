from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    parcel_id = Column(Integer, ForeignKey("parcels.id"), nullable=True)
    action = Column(String, nullable=False)  # e.g., "Qualify", "Disqualify", "Snooze"
    details = Column(Text)  # free-form notes or JSON string
    timestamp = Column(DateTime, default=datetime.utcnow)

    parcel = relationship("Parcel", back_populates="audit_logs")
