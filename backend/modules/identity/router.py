# FastAPI router for the identity module.
# Mounts at /identity. Wires HTTP layer to IdentityService.

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from backend.shared.dependencies import get_db
from backend.modules.identity.repository import UserRepository
from backend.modules.identity.service import IdentityService
from backend.modules.identity.schemas import UserCreate, UserRead
from backend.shared.exceptions import ConflictError

router = APIRouter(prefix="/identity", tags=["identity"])


@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def register(data: UserCreate, db: AsyncSession = Depends(get_db)):
    service = IdentityService(UserRepository(db))
    try:
        user = await service.register(data)
    except ConflictError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return user
