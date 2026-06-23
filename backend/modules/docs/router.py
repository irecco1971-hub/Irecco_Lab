# FastAPI router for the docs module. Mounts at /docs-api.
from fastapi import APIRouter

router = APIRouter(prefix="/docs-api", tags=["docs"])
