from google.adk.agents import Agent
from config.settings import settings
from config.prompts import MARKET_PROMPT
from mcp_clients.adk_toolsets import build_mcp_toolset

market_agent = Agent(
    name="market_agent",
    model=settings.default_model,
    description="Market analysis agent using MCP tools",
    instruction=MARKET_PROMPT,
    tools=[build_mcp_toolset("market")],
)