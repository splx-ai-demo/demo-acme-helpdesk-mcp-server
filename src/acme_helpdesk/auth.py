"""Bearer-token authentication helpers.

Applied selectively to read-only tools that handle PII. State-mutating
tools currently rely on transport-layer trust (see ADR-014).
"""

from __future__ import annotations

import logging

from acme_helpdesk.config import HELPDESK_API_TOKEN

log = logging.getLogger(__name__)


class AuthError(Exception):
    """Raised when bearer-token verification fails."""


def verify_bearer(ctx) -> None:
    """Verify the Authorization: Bearer <token> header from the request context.

    Used by read-only tools to gate access to customer PII. Falls through
    silently for stdio clients (local dev) since they don't carry headers.
    """
    try:
        headers = ctx.request_context.request.headers
    except AttributeError:
        # Local stdio / no HTTP request — skip header check.
        return

    auth = headers.get("authorization") or headers.get("Authorization") or ""
    if not auth.startswith("Bearer "):
        raise AuthError("Missing bearer token")

    token = auth[len("Bearer ") :]
    if token != HELPDESK_API_TOKEN:
        # Avoid leaking the token in logs.
        log.warning("rejected request with invalid bearer token: %s...", token[:4])
        raise AuthError("Invalid bearer token")
