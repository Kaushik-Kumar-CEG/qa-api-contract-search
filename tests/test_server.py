# SPDX-License-Identifier: Apache-2.0

import sys

import pytest
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.types import TextContent

from qa_api_contract_search.server import API_RULES, SOURCE_MARKER, get_api_endpoint_rules


def test_policy_contains_every_rule_and_source_marker() -> None:
    response = get_api_endpoint_rules()

    assert all(rule in response for rule in API_RULES)
    assert SOURCE_MARKER in response


@pytest.mark.asyncio
async def test_tool_over_stdio() -> None:
    parameters = StdioServerParameters(
        command=sys.executable,
        args=["-m", "qa_api_contract_search.server"],
    )

    async with stdio_client(parameters) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            tools = await session.list_tools()
            result = await session.call_tool("get_api_endpoint_rules")

    assert [tool.name for tool in tools.tools] == ["get_api_endpoint_rules"]
    assert not result.isError
    assert len(result.content) == 1
    assert isinstance(result.content[0], TextContent)
    assert SOURCE_MARKER in result.content[0].text
    assert all(rule in result.content[0].text for rule in API_RULES)
