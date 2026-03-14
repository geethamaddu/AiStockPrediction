from google.adk.agents import Agent
from config.settings import settings
from config.prompts import RISK_PROMPT

risk_agent = Agent(
    name="risk_agent",
    model=settings.default_model,
    description="Risk review agent",
    instruction=RISK_PROMPT,
)