# FastAPI router for the products module. Mounts at /products.
from fastapi import APIRouter

router = APIRouter(prefix="/products", tags=["products"])
