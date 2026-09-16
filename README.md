<!-- SPDX-License-Identifier: Apache-2.0 -->

# qa-api-contract-search

A minimal stdio MCP server that returns internal API endpoint contract rules. Every tool response includes the source marker `API CONTRACT SOURCE Q42`.

## Tool

### `get_api_endpoint_rules`

Returns the required API versioning, access control, schema validation, password confirmation, error response, and test coverage rules.

## Requirements

- Python 3.11 or newer
- [uv](https://docs.astral.sh/uv/)

## Run locally

```bash
uv run qa-api-contract-search
```

## MCP configuration

Run directly from GitHub with `uvx`:

```json
{
  "mcpServers": {
    "qa-api-contract-search": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/Kaushik-Kumar-CEG/qa-api-contract-search.git",
        "qa-api-contract-search"
      ]
    }
  }
}
```

## Test

```bash
uv run --extra test pytest
```

## License

Apache License 2.0. See [LICENSE](LICENSE).
