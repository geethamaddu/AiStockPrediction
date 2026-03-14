from memory.context_manager import build_context
from orchestration.workflow import run_data_workflow


class StockOrchestrator:
    def _build_risk_output(self, symbol: str, outputs: dict) -> dict:
        contradictions = []
        risks = []

        market_prev = outputs["market"].get("previous_close", {})
        technical = outputs["technical"].get("moving_averages", {})
        news = outputs["sentiment"].get("news", {})

        if market_prev.get("close") and technical.get("technical_view") == "bearish":
            risks.append("Technical structure remains weak.")

        if len((news or {}).get("articles", [])) == 0:
            risks.append("Limited recent news coverage returned.")

        return {
            "symbol": symbol.upper(),
            "contradictions": contradictions,
            "key_risks": risks or ["No major structural risks detected."],
            "risk_level": "medium" if risks else "low",
        }

    def _build_prediction(self, symbol: str, outputs: dict, risk_output: dict) -> dict:
        score = 0

        tech_view = outputs["technical"]["moving_averages"].get("technical_view")
        if tech_view == "bullish":
            score += 1
        elif tech_view == "bearish":
            score -= 1

        article_count = len(outputs["sentiment"]["news"].get("articles", []))
        if article_count >= 3:
            score += 1

        if outputs["macro"].get("fed_funds_rate", {}).get("value"):
            score += 0

        if risk_output["risk_level"] == "medium":
            score -= 1

        if score >= 1:
            outlook = "bullish"
            confidence = 74
        elif score <= -1:
            outlook = "bearish"
            confidence = 68
        else:
            outlook = "neutral"
            confidence = 60

        return {
            "symbol": symbol.upper(),
            "outlook": outlook,
            "confidence": confidence,
            "summary": f"{symbol.upper()} has a {outlook} outlook based on dynamic MCP-fed market, technical, news, and macro signals.",
            "supporting_signals": [
                f"Technical view: {tech_view}",
                f"Recent news count: {article_count}",
                f"Risk level: {risk_output['risk_level']}",
            ],
            "risk_factors": risk_output["key_risks"],
            "agent_outputs": {
                **outputs,
                "risk": risk_output,
                "context": build_context(symbol.upper(), outputs),
            },
        }

    def analyze(self, symbol: str) -> dict:
        outputs = run_data_workflow(symbol)
        risk_output = self._build_risk_output(symbol, outputs)
        return self._build_prediction(symbol, outputs, risk_output)