from pydantic import BaseModel


class PredictResponse(BaseModel):
    symbol: str
    outlook: str
    confidence: int
    summary: str
    supporting_signals: list[str]
    risk_factors: list[str]
    agent_outputs: dict