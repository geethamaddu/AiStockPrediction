import os
import requests
from fastapi import APIRouter
from api.schemas import PredictResponse
from orchestration.orchestrator import StockOrchestrator

router = APIRouter()
orchestrator = StockOrchestrator()

POLYGON_API_KEY = os.getenv("POLYGON_API_KEY", "")
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY", "")
FRED_API_KEY = os.getenv("FRED_API_KEY", "")


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.get("/predict/{symbol}", response_model=PredictResponse)
def predict(symbol: str):
    return orchestrator.analyze(symbol)


@router.get("/internal/tools/{symbol}")
def internal_tools(symbol: str):
    symbol = symbol.upper()

    # In a real ADK runtime flow, these would be invoked via MCP tool calls through agent execution.
    # This internal endpoint keeps the demo easy to run while the tools themselves stay MCP-based.

    market_data = requests.get(
        f"https://api.polygon.io/v2/aggs/ticker/{symbol}/prev?adjusted=true&apiKey={POLYGON_API_KEY}",
        timeout=20,
    ).json() if POLYGON_API_KEY else {"error": "Missing POLYGON_API_KEY"}

    last_trade = requests.get(
        f"https://api.polygon.io/v2/last/trade/{symbol}?apiKey={POLYGON_API_KEY}",
        timeout=20,
    ).json() if POLYGON_API_KEY else {"error": "Missing POLYGON_API_KEY"}

    news = requests.get(
        "https://newsapi.org/v2/everything",
        params={"q": symbol, "sortBy": "publishedAt", "pageSize": 5, "language": "en", "apiKey": NEWSAPI_KEY},
        timeout=20,
    ).json() if NEWSAPI_KEY else {"error": "Missing NEWSAPI_KEY"}

    def fred(series_id: str):
        if not FRED_API_KEY:
            return {"error": "Missing FRED_API_KEY"}
        return requests.get(
            "https://api.stlouisfed.org/fred/series/observations",
            params={
                "series_id": series_id,
                "api_key": FRED_API_KEY,
                "file_type": "json",
                "sort_order": "desc",
                "limit": 1,
            },
            timeout=20,
        ).json()

    return {
        "market": {
            "last_trade": last_trade,
            "previous_close": market_data,
        },
        "technical": {
            "moving_averages": {"symbol": symbol, "technical_view": "neutral"}
        },
        "sentiment": {
            "news": {
                "articles": news.get("articles", [])[:5] if isinstance(news, dict) else []
            }
        },
        "macro": {
            "fed_funds_rate": fred("FEDFUNDS"),
            "cpi": fred("CPIAUCSL"),
            "unemployment": fred("UNRATE"),
        },
    }