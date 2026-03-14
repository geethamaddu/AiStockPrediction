class SessionStore:
    def __init__(self):
        self._sessions = {}

    def save(self, session_id: str, payload: dict) -> None:
        self._sessions[session_id] = payload

    def get(self, session_id: str):
        return self._sessions.get(session_id)