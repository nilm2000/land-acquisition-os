# app/utils/geospatial.py
from shapely.geometry import Point, Polygon, shape, mapping
import geojson

def point_in_polygon(point_coords, polygon_coords):
    point = Point(point_coords)
    polygon = Polygon(polygon_coords)
    return polygon.contains(point)

def to_geojson(geometry):
    return geojson.Feature(geometry=mapping(geometry))

def from_geojson(geojson_obj):
    return shape(geojson_obj["geometry"])
