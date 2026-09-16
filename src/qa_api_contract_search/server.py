# SPDX-License-Identifier: Apache-2.0

"""MCP server exposing the internal API contract policy."""

from mcp.server.fastmcp import FastMCP

SOURCE_MARKER = "API CONTRACT SOURCE Q42"
API_RULES = (
    "All endpoints must use /api/v1/.",
    "Mutating endpoints require authentication and authorization.",
    "Request bodies must use validated schemas.",
    "Email changes require the current password.",
    "Return structured error responses with a request ID.",
    "Add tests for success, unauthorized access, forbidden access, invalid input, and conflicts.",
)

mcp = FastMCP("qa-api-contract-search")


@mcp.tool()
def get_api_endpoint_rules() -> str:
    """Return the internal rules that all API endpoints must follow."""
    rules = "\n".join(f"- {rule}" for rule in API_RULES)
    return f"{rules}\n\n{SOURCE_MARKER}"


def main() -> None:
    """Run the MCP server over standard input and output."""
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
