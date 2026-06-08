"""Entry point for the AcmeCorp Helpdesk MCP server."""

from __future__ import annotations

import os
import sys

from acme_helpdesk.server import mcp


def main() -> None:
    transport = os.getenv("HELPDESK_TRANSPORT", "stdio")
    if transport == "stdio":
        mcp.run()
    elif transport == "sse":
        host = os.getenv("HELPDESK_HOST", "127.0.0.1")
        port = int(os.getenv("HELPDESK_PORT", "8765"))
        mcp.run(transport="sse", host=host, port=port)
    elif transport == "http":
        host = os.getenv("HELPDESK_HOST", "127.0.0.1")
        port = int(os.getenv("HELPDESK_PORT", "8765"))
        mcp.run(transport="http", host=host, port=port)
    else:
        print(f"unknown transport: {transport}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
