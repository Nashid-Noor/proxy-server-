# Proxy Server - Expense Tracker

This is an MCP Proxy Server that connects to the remotely deployed **Expense Tracker**.

It allows you to test and interact with the remote `expense-tracker-remoteserver` as if it were running locally, forwarding all MCP tool and resource requests.

## Configuration

The server acts as a proxy to:
`https://expense-tracker-remoteserver.fastmcp.app/mcp`

## Running

You can run this using `uv`:

```bash
uv run fastmcp dev main.py
```
