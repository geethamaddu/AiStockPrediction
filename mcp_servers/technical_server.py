import os
import requests
from statistics import mean
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("technical-server")
POLYGON_API_KEY = os.getenv("POLYGON_API_KEY", "")


def _close_series(symbol: str, limit: int = 60) -> list[float]:
    url = f"https://api.polygon.io/v2/aggs/ticker/{symbol.upper()}/range/1/day/2025-01-01/2026-12-31?adjusted=true&sort=desc&limit={limit}&apiKey={POLYGON_API_KEY}"
    response = requests.get(url, timeout=20)
    response.raise_for_status()
    data = response.json()
    return [item["c"] for item in data.get("results", []) if "c" in item][::-1]


@mcp.tool()
def get_moving_averages(symbol: str) -> dict:
    if not POLYGON_API_KEY:
        return {"symbol": symbol.upper(), "error": "Missing POLYGON_API_KEY"}

    closes = _close_series(symbol, 60)
    if len(closes) < 50:
        return {"symbol": symbol.upper(), "error": "Not enough price history"}

    sma_20 = mean(closes[-20:])
    sma_50 = mean(closes[-50:])
    latest = closes[-1]

    view = "bullish" if latest > sma_20 > sma_50 else "bearish" if latest < sma_20 < sma_50 else "neutral"
    return {
        "symbol": symbol.upper(),
        "latest_close": latest,
        "sma_20": round(sma_20, 2),
        "sma_50": round(sma_50, 2),
        "technical_view": view,
    }


if __name__ == "__main__":
    mcp.run(transport="stdio")