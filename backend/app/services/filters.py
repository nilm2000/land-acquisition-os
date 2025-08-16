"""
Service for applying saved filters to a parcel queryset.
"""
from sqlalchemy.orm import Query
from app import models


def apply_filter(query: Query, filter_obj: models.Filter):
    if filter_obj.min_acreage:
        query = query.filter(models.Parcel.acreage >= filter_obj.min_acreage)
    if filter_obj.max_acreage:
        query = query.filter(models.Parcel.acreage <= filter_obj.max_acreage)
    if filter_obj.city:
        query = query.filter(models.Parcel.city == filter_obj.city)
    if filter_obj.state:
        query = query.filter(models.Parcel.state == filter_obj.state)
    return query
