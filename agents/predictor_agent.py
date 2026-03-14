from google.adk.agents import Agent
from config.settings import settings
from config.prompts import PREDICTOR_PROMPT

predictor_agent = Agent(
    name="predictor_agent",
    model=settings.default_model,
    description="Final prediction synthesis agent",
    instruction=PREDICTOR_PROMPT,
)