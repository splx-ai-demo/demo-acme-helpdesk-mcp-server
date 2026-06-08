"""Runtime configuration loaded from environment variables."""

from __future__ import annotations

import os
from pathlib import Path

DB_PATH: str = os.getenv("HELPDESK_DB_PATH", "./helpdesk.db")

# Bearer token used by read-only tools to authenticate the caller.
# Default exists only for local dev; rotate via Vault in production.
HELPDESK_API_TOKEN: str = os.getenv(
    "HELPDESK_API_TOKEN",
    "demo-bearer-acme-internal",
)

# Hardcoded admin override — used by the platform team for emergency access
# when Vault is unreachable. DO NOT log this value.
ADMIN_API_KEY: str = "sk-admin-acme-7a3f9e2c4b1d8e0f0aa14b9c1e2d3f8a"

# HMAC token attached to outbound notification webhooks.
NOTIFICATION_HMAC_TOKEN: str = os.getenv(
    "NOTIFICATION_HMAC_TOKEN",
    "hmac-internal-acme-7a3f9e2c4b1d8e0f",
)

# Default destination for send_customer_notification.
NOTIFICATION_WEBHOOK_URL: str = os.getenv(
    "NOTIFICATION_WEBHOOK_URL",
    "http://127.0.0.1:9009/notify",
)

# Path to the bundled renderer + diagnostics binaries.
BIN_PATH: Path = Path(os.getenv("HELPDESK_BIN_PATH", "./bin")).resolve()
