# FastAPI router for the notifications module. Mounts at /notifications.
from fastapi import APIRouter

router = APIRouter(prefix="/notifications", tags=["notifications"])
