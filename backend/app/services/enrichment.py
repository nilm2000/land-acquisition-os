"""
Handles parcel enrichment using external APIs like Regrid.
"""
import os
import requests
from typing import Optional

REGRID_API_KEY = os.getenv("REGRID_API_KEY", "")
REGRID_BASE_URL = "https://app.regrid.com/api/v1"


def get_parcel_from_regrid(apn: Optional[str] = None, lat: Optional[float] = None, lon: Optional[float] = None):
    """
    Fetch parcel details from Regrid API using APN or coordinates.
    """
    if not REGRID_API_KEY:
        raise ValueError("Regrid API key is not configured.")

    params = {"token": REGRID_API_KEY}
    if apn:
        params["apn"] = apn
    elif lat and lon:
        params["lat"] = lat
        params["lon"] = lon
    else:
        raise ValueError("You must provide either an APN or coordinates.")

    resp = requests.get(f"{REGRID_BASE_URL}/parcels", params=params)
    resp.raise_for_status()
    return resp.json()


def enrich_parcel_with_regrid(parcel_record: dict):
    """
    Takes a parcel dict and enriches it with Regrid data.
    """
    try:
        data = get_parcel_from_regrid(
            apn=parcel_record.get("apn"),
            lat=parcel_record.get("lat"),
            lon=parcel_record.get("lon")
        )
        parcel_record.update(data)
        return parcel_record
    except Exception as e:
        return {"error": str(e)}
