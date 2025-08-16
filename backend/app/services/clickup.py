"""
Handles sending data to ClickUp task management API.
"""
import os
import requests

CLICKUP_API_KEY = os.getenv("CLICKUP_API_KEY", "")
CLICKUP_BASE_URL = "https://api.clickup.com/api/v2"


def create_clickup_task(list_id: str, name: str, description: str):
    if not CLICKUP_API_KEY:
        raise ValueError("ClickUp API key is not configured.")

    headers = {"Authorization": CLICKUP_API_KEY}
    payload = {
        "name": name,
        "description": description,
        "status": "to do"
    }
    resp = requests.post(f"{CLICKUP_BASE_URL}/list/{list_id}/task", headers=headers, json=payload)
    resp.raise_for_status()
    return resp.json()
