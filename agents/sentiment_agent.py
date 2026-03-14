from google.adk.agents import Agent
from config.settings import settings
from config.prompts import SENTIMENT_PROMPT
from mcp_clients.adk_toolsets import build_mcp_toolset

sentiment_agent = Agent(
    name="sentiment_agent",
    model=settings.default_model,
    description="Sentiment agent using MCP tools",
    instruction=SENTIMENT_PROMPT,
    tools=[build_mcp_toolset("news")],
)