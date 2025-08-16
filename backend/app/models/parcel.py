from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Parcel(Base):
    __tablename__ = "parcels"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, nullable=True)
    city = Column(String, nullable=True)
    state = Column(String, nullable=True)
    zip = Column(String, nullable=True)
    apn = Column(String, nullable=True)
    county_fips = Column(String, nullable=True)
    price = Column(Float, nullable=True)
    acreage = Column(Float, nullable=True)
    zoning = Column(String, nullable=True)
    flood_percent = Column(Float, nullable=True)
    wetlands_percent = Column(Float, nullable=True)
    slope_mean = Column(Float, nullable=True)
    slope_p95 = Column(Float, nullable=True)
    status = Column(String, default="Unqualified")
