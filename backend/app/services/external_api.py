import os
import httpx

API_BASE_URL = os.getenv("EXTERNAL_API_URL", "https://example.com/api")
API_KEY = os.getenv("EXTERNAL_API_KEY", None)

async def fetch_data(params: dict):
    """
    Placeholder function to fetch data from an external API.
    Change URL and params when you choose a provider.
    """
    if not API_KEY:
        raise ValueError("EXTERNAL_API_KEY not configured in .env")

    async with httpx.AsyncClient(timeout=30) as client:
        response = await client.get(
            API_BASE_URL,
            params={**params, "api_key": API_KEY}
        )
        response.raise_for_status()
        return response.json()
