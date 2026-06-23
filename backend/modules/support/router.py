# FastAPI router for the support module. Mounts at /support.
from fastapi import APIRouter

router = APIRouter(prefix="/support", tags=["support"])
