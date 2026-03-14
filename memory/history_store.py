class HistoryStore:
    def __init__(self):
        self._history = []

    def add(self, entry: dict) -> None:
        self._history.append(entry)

    def list(self) -> list:
        return self._history