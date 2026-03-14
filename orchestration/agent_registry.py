from agents.market_agent import market_agent
from agents.technical_agent import technical_agent
from agents.sentiment_agent import sentiment_agent
from agents.macro_agent import macro_agent
from agents.risk_agent import risk_agent
from agents.predictor_agent import predictor_agent


def get_agent_registry() -> dict:
    return {
        "market": market_agent,
        "technical": technical_agent,
        "sentiment": sentiment_agent,
        "macro": macro_agent,
        "risk": risk_agent,
        "predictor": predictor_agent,
    }