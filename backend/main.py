# Entry point for the Irecco Lab FastAPI application.
# Registers all module routers and initialises middleware.

from fastapi import FastAPI

from backend.modules.identity.router import router as identity_router
from backend.modules.products.router import router as products_router
from backend.modules.beta_program.router import router as beta_router
from backend.modules.support.router import router as support_router
from backend.modules.docs.router import router as docs_router
from backend.modules.notifications.router import router as notifications_router

app = FastAPI(title="Irecco Lab", version="0.1.0")

app.include_router(identity_router)
app.include_router(products_router)
app.include_router(beta_router)
app.include_router(support_router)
app.include_router(docs_router)
app.include_router(notifications_router)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
