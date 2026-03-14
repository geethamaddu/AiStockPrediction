import os
import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("market-data-server")
POLYGON_API_KEY = os.getenv("POLYGON_API_KEY", "")


@mcp.tool()
def get_last_trade(symbol: str) -> dict:
    symbol = symbol.upper()
    if not POLYGON_API_KEY:
        return {
            "symbol": symbol,
            "error": "Missing POLYGON_API_KEY",
        }

    url = f"https://api.polygon.io/v2/last/trade/{symbol}?apiKey={POLYGON_API_KEY}"
    response = requests.get(url, timeout=20)
    response.raise_for_status()
    data = response.json()

    results = data.get("results", {})
    return {
        "symbol": symbol,
        "price": results.get("p"),
        "size": results.get("s"),
        "exchange": results.get("x"),
        "timestamp": results.get("t"),
    }


@mcp.tool()
def get_previous_close(symbol: str) -> dict:
    symbol = symbol.upper()
    if not POLYGON_API_KEY:
        return {
            "symbol": symbol,
            "error": "Missing POLYGON_API_KEY",
        }
    url = f"https://api.polygon.io/v2/aggs/ticker/{symbol}/prev?adjusted=true&apiKey={POLYGON_API_KEY}"
    response = requests.get(url, timeout=20)
    response.raise_for_status()
    data = response.json()
    result = (data.get("results") or [{}])[0]

    return {
        "symbol": symbol,
        "close": result.get("c"),
        "open": result.get("o"),
        "high": result.get("h"),
        "low": result.get("l"),
        "volume": result.get("v"),
    }


if __name__ == "__main__":
    mcp.run(transport="stdio")