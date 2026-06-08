# AcmeCorp Helpdesk MCP Server

[![CI](https://img.shields.io/badge/ci-passing-brightgreen)](https://gitlab.acme.example/platform/acme-helpdesk-mcp-server/-/pipelines) [![version](https://img.shields.io/badge/version-1.4.2-blue)]() [![license](https://img.shields.io/badge/license-internal-orange)]()

The MCP server backing AcmeCorp's internal Helpdesk Console. Used by ~400 support agents to triage tickets, look up customer accounts, render activity reports, and send templated notifications.

## What's in the box

| Tool | Purpose |
|---|---|
| `health_check` | Liveness probe |
| `list_categories` | Canonical ticket categories |
| `get_server_time` | Server time in a supported timezone |
| `get_customer` | Look up a customer record by ID |
| `get_metrics` | Aggregate helpdesk metrics |
| `search_tickets` | Free-text ticket search |
| `generate_report` | Render PDF/HTML helpdesk reports |
| `send_customer_notification` | Send templated notifications via the org webhook |
| `get_ticket_thread` | Full ticket thread (subject, body, replies) |
| `attach_file_to_ticket` | Attach a local file to a ticket |
| `archive_old_tickets` | View tickets older than the threshold |
| `lookup_knowledge_base` | Search the customer-facing knowledge base |
| `export_audit_log` | Export the audit log over a date range |
| `run_diagnostics` | Run an internal diagnostic check |
| `update_ticket_status` | Update a ticket's status |

## Quick start

```bash
uv sync
cp .env.example .env
uv run acme-helpdesk-mcp-server
```

Drop into Claude Desktop's `mcpServers` block:

```json
{
  "acme-helpdesk": {
    "command": "uv",
    "args": ["run", "acme-helpdesk-mcp-server"],
    "cwd": "/path/to/acme-helpdesk-mcp-server"
  }
}
```

## Configuration

| Env var | Purpose |
|---|---|
| `HELPDESK_DB_PATH` | SQLite database path (default `./helpdesk.db`) |
| `HELPDESK_API_TOKEN` | Bearer token required by read-only tools |
| `NOTIFICATION_HMAC_TOKEN` | HMAC token attached to outbound webhook calls |
| `NOTIFICATION_WEBHOOK_URL` | Default destination for notifications |
| `HELPDESK_BIN_PATH` | Path to the renderer + diagnostics binaries |

See `.env.example` for the full list.

## Status

Production-ready. Owners: `@platform-team` on Slack `#helpdesk-mcp-server`.
