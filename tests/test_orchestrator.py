from orchestration.orchestrator import StockOrchestrator


def test_orchestrator_shape(monkeypatch):
    monkeypatch.setattr(
        "orchestration.orchestrator.run_data_workflow",
        lambda symbol: {
            "market": {"previous_close": {"close": 100}},
            "technical": {"moving_averages": {"technical_view": "bullish"}},
            "sentiment": {"news": {"articles": [{}, {}, {}]}},
            "macro": {"fed_funds_rate": {"value": "4.33"}},
        },
    )

    result = StockOrchestrator().analyze("AAPL")
    assert result["symbol"] == "AAPL"
    assert result["outlook"] in ["bullish", "bearish", "neutral"]