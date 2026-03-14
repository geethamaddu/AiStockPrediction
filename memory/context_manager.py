def build_context(symbol: str, outputs: dict) -> str:
    return (
        f"Symbol: {symbol}"

        f"Market: {outputs.get('market')}"

        f"Technical: {outputs.get('technical')}"

        f"Sentiment: {outputs.get('sentiment')}"

        f"Macro: {outputs.get('macro')}"

    )