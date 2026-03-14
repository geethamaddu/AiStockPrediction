import os
import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("macro-server")
FRED_API_KEY = os.getenv("FRED_API_KEY", "")
FRED_BASE = "https://api.stlouisfed.org/fred/series/observations"


def _fred_latest(series_id: str) -> dict:
    params = {
        "series_id": series_id,
        "api_key": FRED_API_KEY,
        "file_type": "json",
        "sort_order": "desc",
        "limit": 1,
    }
    response = requests.get(FRED_BASE, params=params, timeout=20)
    response.raise_for_status()
    data = response.json()
    obs = (data.get("observations") or [{}])[0]
    return {
        "series_id": series_id,
        "date": obs.get("date"),
        "value": obs.get("value"),
    }


@mcp.tool()
def get_fed_funds_rate() -> dict:
    if not FRED_API_KEY:
        return {"error": "Missing FRED_API_KEY"}
    return _fred_latest("FEDFUNDS")


@mcp.tool()
def get_cpi() -> dict:
    if not FRED_API_KEY:
        return {"error": "Missing FRED_API_KEY"}
    return _fred_latest("CPIAUCSL")


@mcp.tool()
def get_unemployment_rate() -> dict:
    if not FRED_API_KEY:
        return {"error": "Missing FRED_API_KEY"}
    return _fred_latest("UNRATE")


if __name__ == "__main__":
    mcp.run(transport="stdio")