from google.adk.agents import Agent
from config.settings import settings
from config.prompts import TECHNICAL_PROMPT
from mcp_clients.adk_toolsets import build_mcp_toolset

technical_agent = Agent(
    name="technical_agent",
    model=settings.default_model,
    description="Technical analysis agent using MCP tools",
    instruction=TECHNICAL_PROMPT,
    tools=[build_mcp_toolset("technical")],
)