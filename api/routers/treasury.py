import logging
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from api.services.circle_service import create_wallet_set, create_wallet
from api.utils.persistence import save_config, load_config

logger = logging.getLogger(__name__)
router = APIRouter()

class Wallet(BaseModel):
    id: str
    address: str
    blockchain: str
    state: str
    createDate: str  # Matches Circle's API response key

class SetupRequest(BaseModel):
    name: str = "Pulse Ledger Treasury"
    blockchains: list[str] = ["MATIC-AMOY"]
    count: int = 1

class SetupResponse(BaseModel):
    wallet_set_id: str
    wallets: list[Wallet]

@router.post("/setup", response_model=SetupResponse)
async def setup_treasury(req: SetupRequest):
    # 1. Check for persistence first
    existing_config = load_config()
    if existing_config:
        logger.info("Existing treasury config found. Loading from disk.")
        # FastAPI will automatically validate this dict against SetupResponse
        return existing_config

    try:
        # 2. Sequence: Set -> Wallet
        wallet_set_id = create_wallet_set(req.name)
        
        # Security: In production, you'd check if wallet_set_id is an error string
        if "Error" in wallet_set_id:
             raise ValueError(wallet_set_id)

        wallets_data = create_wallet(
            wallet_set_id, 
            blockchains=req.blockchains, 
            count=req.count
        )

        config_data = {
            "wallet_set_id": wallet_set_id,
            "wallets": wallets_data
        }
        
        # 3. Save for future reloads
        save_config(config_data)
        
        return config_data

    except Exception as e:
        logger.exception("Treasury setup failed")
        raise HTTPException(
            status_code=500, 
            detail=f"Failed to initialize Circle Ledger: {str(e)}"
        )