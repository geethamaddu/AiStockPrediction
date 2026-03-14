from google.adk.tools.mcp_tool.mcp_toolset import McpToolset, StdioServerParameters
from mcp_clients.server_config import MCP_SERVER_COMMANDS


def build_mcp_toolset(server_name: str) -> McpToolset:
    config = MCP_SERVER_COMMANDS[server_name]
    return McpToolset(
        connection_params=StdioServerParameters(
            command=config["command"],
            args=config["args"],
        )
    )