# Application-wide exception classes.
# Raise these from service / use-case layer; handle them in routers or middleware.


class NotFoundError(Exception):
    """Raised when a requested resource does not exist."""


class PermissionDeniedError(Exception):
    """Raised when the caller lacks the required permission."""


class ConflictError(Exception):
    """Raised when an operation conflicts with existing state (e.g. duplicate)."""
