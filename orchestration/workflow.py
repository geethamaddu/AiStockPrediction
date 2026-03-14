import os
import requests


def run_data_workflow(symbol: str) -> dict:
    base = os.getenv("APP_BASE_URL", "http://localhost:8000")
    response = requests.get(f"{base}/internal/tools/{symbol.upper()}", timeout=60)
    response.raise_for_status()
    return response.json()