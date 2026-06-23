# Reusable FastAPI dependencies (db session, current user, etc.).
# Import individual dependencies in module routers as needed.

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError
from sqlalchemy.ext.asyncio import AsyncSession

from backend.database import get_db
from backend.shared.security import decode_access_token

__all__ = ["get_db", "get_current_user"]

_bearer = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(_bearer),
    db: AsyncSession = Depends(get_db),
):
    # Import here to avoid circular imports between shared and identity.
    from backend.modules.identity.repository import UserRepository
    import uuid

    token = credentials.credentials
    try:
        user_id = decode_access_token(token)
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user = await UserRepository(db).get_by_id(uuid.UUID(user_id))
    if not user or not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found or inactive.",
        )
    return user
