from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Simple model for our first OOAD test
class TradeRequest(BaseModel):
    origin: str
    destination: str
    amount: float

@app.get("/api/python")
def hello_world():
    return {"message": "Pulse Agent is online and ready for African trade settlement."}

@app.post("/api/check-compliance")
def check_compliance(request: TradeRequest):
    # This is where your PulseAgent class will eventually live
    # For now, we return a mock success
    return {
        "status": "compliant",
        "route": f"{request.origin} -> {request.destination}",
        "fee_reduction": "4.2%",
        "message": "AfCFTA protocols verified."
    }