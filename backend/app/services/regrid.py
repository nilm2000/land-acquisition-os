# app/services/regrid.py
import os
import requests
from typing import Optional, Dict

REGRID_API_KEY = os.getenv("REGRID_API_KEY", "")

BASE_URL = "https://app.regrid.com/api/v1"


def get_parcel_by_apn(apn: str, county_fips: str) -> Optional[Dict]:
    """
    Fetch parcel data from Regrid API given APN & county FIPS.
    """
    if not REGRID_API_KEY:
        raise RuntimeError("REGRID_API_KEY is not set in environment variables.")

    url = f"{BASE_URL}/parcels/search"
    params = {
        "search": apn,
        "county_fips": county_fips,
        "apikey": REGRID_API_KEY
    }
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    data = resp.json()

    if not data.get("features"):
        return None

    return data["features"][0]["properties"]


def enrich_parcel(parcel):
    """
    Given a Parcel ORM object, enrich it with Regrid data.
    """
    if not parcel.apn or not parcel.county_fips:
        return parcel  # Can't enrich without APN + county FIPS

    try:
        regrid_data = get_parcel_by_apn(parcel.apn, parcel.county_fips)
        if not regrid_data:
            return parcel

        parcel.zoning = regrid_data.get("zoning")
        parcel.acreage = regrid_data.get("acres")
        parcel.address = regrid_data.get("address")
        parcel.city = regrid_data.get("city")
        parcel.state = regrid_data.get("state")
        parcel.zip = regrid_data.get("zip")
        # Add any other mapping as needed

    except Exception as e:
        print(f"Error enriching parcel {parcel.id}: {e}")

    return parcel
