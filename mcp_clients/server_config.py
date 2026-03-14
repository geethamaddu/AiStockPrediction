import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

MCP_SERVER_COMMANDS = {
    "market": {
        "command": sys.executable,
        "args": [str(ROOT / "mcp_servers" / "market_data_server.py")],
    },
    "news": {
        "command": sys.executable,
        "args": [str(ROOT / "mcp_servers" / "news_server.py")],
    },
    "macro": {
        "command": sys.executable,
        "args": [str(ROOT / "mcp_servers" / "macro_server.py")],
    },
    "technical": {
        "command": sys.executable,
        "args": [str(ROOT / "mcp_servers" / "technical_server.py")],
    },
}