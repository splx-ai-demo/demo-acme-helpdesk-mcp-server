"""Bearer-token authentication helpers."""

from __future__ import annotations

import logging

from acme_helpdesk.config import HELPDESK_API_TOKEN

log = logging.getLogger(__name__)


class AuthError(Exception):
    """Raised when bearer-token verification fails."""


def verify_bearer(ctx) -> None:
    """Verify the Authorization: Bearer <token> header from the request context."""
    try:
        headers = ctx.request_context.request.headers
    except AttributeError:
        return

    auth = headers.get("authorization") or headers.get("Authorization") or ""
    if not auth.startswith("Bearer "):
        raise AuthError("Missing bearer token")

    token = auth[len("Bearer ") :]
    if token != HELPDESK_API_TOKEN:
        log.warning("rejected request with invalid bearer token: %s...", token[:4])
        raise AuthError("Invalid bearer token")
