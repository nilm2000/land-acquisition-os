from sqlalchemy import Column, Integer, String, ForeignKey, JSON, Float
from sqlalchemy.orm import relationship
from app.database import Base


class Filter(Base):
    __tablename__ = "filters"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)

    name = Column(String, nullable=False)
    polygon_geojson = Column(JSON, nullable=False)
    rules = Column(JSON)  # Store all min/max values, zoning whitelist/blacklist, etc.

    # Optional reference points for "distance from point"
    reference_points = Column(JSON)  # e.g., [{"lat": 40.1, "lon": -74.2}]

    project = relationship("Project", back_populates="filters")
