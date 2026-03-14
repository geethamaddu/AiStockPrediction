import os
import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("news-server")
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY", "")


@mcp.tool()
def get_company_news(symbol: str) -> dict:
    symbol = symbol.upper()
    if not NEWSAPI_KEY:
        return {"symbol": symbol, "error": "Missing NEWSAPI_KEY"}

    query = symbol
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "sortBy": "publishedAt",
        "pageSize": 5,
        "language": "en",
        "apiKey": NEWSAPI_KEY,
    }

    response = requests.get(url, params=params, timeout=20)
    response.raise_for_status()
    data = response.json()

    articles = []
    for article in data.get("articles", [])[:5]:
        articles.append(
            {
                "title": article.get("title"),
                "source": (article.get("source") or {}).get("name"),
                "published_at": article.get("publishedAt"),
                "url": article.get("url"),
            }
        )

    return {"symbol": symbol, "articles": articles}


if __name__ == "__main__":
    mcp.run(transport="stdio")