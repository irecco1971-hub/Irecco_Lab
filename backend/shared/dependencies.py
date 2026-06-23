# Reusable FastAPI dependencies (db session, current user, etc.).
# Import individual dependencies in module routers as needed.

from backend.database import get_db  # re-exported for convenience

__all__ = ["get_db"]
