from google.adk.agents import Agent
from config.settings import settings
from config.prompts import MACRO_PROMPT
from mcp_clients.adk_toolsets import build_mcp_toolset

macro_agent = Agent(
    name="macro_agent",
    model=settings.default_model,
    description="Macro agent using MCP tools",
    instruction=MACRO_PROMPT,
    tools=[build_mcp_toolset("macro")],
)