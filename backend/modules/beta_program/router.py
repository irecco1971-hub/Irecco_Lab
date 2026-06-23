# FastAPI router for the beta_program module. Mounts at /beta.
from fastapi import APIRouter

router = APIRouter(prefix="/beta", tags=["beta_program"])
