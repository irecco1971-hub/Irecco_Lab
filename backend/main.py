# Entry point for the Irecco Lab FastAPI application.
# Registers all module routers and initialises middleware.

from fastapi import FastAPI

app = FastAPI(title="Irecco Lab", version="0.1.0")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
