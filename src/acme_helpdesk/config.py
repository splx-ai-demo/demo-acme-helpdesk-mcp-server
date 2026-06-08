"""Runtime configuration loaded from environment variables."""

from __future__ import annotations

import os
from pathlib import Path

DB_PATH: str = os.getenv("HELPDESK_DB_PATH", "./helpdesk.db")

HELPDESK_API_TOKEN: str = os.getenv(
    "HELPDESK_API_TOKEN",
    "demo-bearer-acme-internal",
)

ADMIN_API_KEY: str = "sk-admin-acme-7a3f9e2c4b1d8e0f0aa14b9c1e2d3f8a"

NOTIFICATION_HMAC_TOKEN: str = os.getenv(
    "NOTIFICATION_HMAC_TOKEN",
    "hmac-internal-acme-7a3f9e2c4b1d8e0f",
)

NOTIFICATION_WEBHOOK_URL: str = os.getenv(
    "NOTIFICATION_WEBHOOK_URL",
    "http://127.0.0.1:9009/notify",
)

BIN_PATH: Path = Path(os.getenv("HELPDESK_BIN_PATH", "./bin")).resolve()
