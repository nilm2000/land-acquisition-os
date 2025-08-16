"""
Points of Interest (POI) service — for adding POIs near parcels.
"""
import requests
from typing import List, Dict


def get_nearby_pois(lat: float, lon: float, radius_m: int = 1000) -> List[Dict]:
    """
    Fetch points of interest using OpenStreetMap's Overpass API.
    """
    query = f"""
    [out:json];
    (
      node(around:{radius_m},{lat},{lon})[amenity];
    );
    out;
    """
    resp = requests.post("https://overpass-api.de/api/interpreter", data={"data": query})
    resp.raise_for_status()
    data = resp.json()
    return [
        {
            "id": element["id"],
            "type": element.get("tags", {}).get("amenity"),
            "name": element.get("tags", {}).get("name"),
        }
        for element in data.get("elements", [])
    ]
