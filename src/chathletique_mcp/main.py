"""MCP Server Template"""

from .mcp_utils import mcp

# Import modules containing MCP tools to register them
from . import strava_tools  # noqa: F401
from . import weather_tools  # noqa: F401

def main():
    """Main entry point for the MCP server."""
    mcp.run(transport="streamable-http", port=3000, stateless_http=True)


if __name__ == "__main__":
    main()
