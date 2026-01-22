# main.py
from fastapi import FastAPI
from api.routers import treasury  # import your treasury router

app = FastAPI(
    title="Pulse Ledger API",
    description="Autonomous escrow & treasury management for agentic commerce",
    version="1.0.0"
)

# Register routers
app.include_router(
    treasury.router,
    prefix="/api/treasury",
    tags=["treasury"]
)

@app.get("/")
def root():
    return {"message": "Pulse Ledger API is running"}
