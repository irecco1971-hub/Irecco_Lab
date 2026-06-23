# FastAPI router for the identity module. Mounts at /identity.

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from backend.shared.dependencies import get_db
from backend.shared.exceptions import ConflictError, PermissionDeniedError
from backend.modules.identity.repository import UserRepository
from backend.modules.identity.service import IdentityService
from backend.modules.identity.schemas import LoginRequest, TokenResponse, UserCreate, UserRead

router = APIRouter(prefix="/identity", tags=["identity"])


def _service(db: AsyncSession = Depends(get_db)) -> IdentityService:
    return IdentityService(UserRepository(db))


@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def register(data: UserCreate, svc: IdentityService = Depends(_service)):
    try:
        return await svc.register(data)
    except ConflictError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))


@router.post("/login", response_model=TokenResponse)
async def login(data: LoginRequest, svc: IdentityService = Depends(_service)):
    try:
        token = await svc.login(data.email, data.password)
    except PermissionDeniedError as exc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(exc))
    return TokenResponse(access_token=token)
