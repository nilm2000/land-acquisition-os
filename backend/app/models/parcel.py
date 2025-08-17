from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Parcel(Base):
    __tablename__ = "parcels"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, nullable=False)
    owner_name = Column(String, nullable=True)
    parcel_id = Column(String, unique=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User")
