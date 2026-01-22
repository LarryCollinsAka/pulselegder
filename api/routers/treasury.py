import logging
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from api.services.circle_service import create_wallet_set, create_wallet, transfer_tokens
from api.utils.persistence import save_config, load_config

logger = logging.getLogger(__name__)
router = APIRouter()

# -----------------------------
# Pydantic Models
# -----------------------------
class Wallet(BaseModel):
    id: str
    address: str
    blockchain: str
    state: str
    createDate: str

class SetupRequest(BaseModel):
    name: str = "Pulse Ledger Treasury"
    blockchains: list[str] = ["MATIC-AMOY"]
    count: int = 1

class SetupResponse(BaseModel):
    wallet_set_id: str
    wallets: list[Wallet]

class TransferRequest(BaseModel):
    source_wallet_id: str
    destination_address: str
    amount: int  # base units (1 USDC = 1000000)

class TransferResponse(BaseModel):
    transactionId: str
    hash: str
    status: str

# -----------------------------
# Routes
# -----------------------------

@router.post("/setup", response_model=SetupResponse)
async def setup_treasury(req: SetupRequest):
    existing_config = load_config()
    if existing_config:
        logger.info("Existing treasury config found. Returning persisted config.")
        return existing_config

    try:
        wallet_set_id = create_wallet_set(req.name)
        if isinstance(wallet_set_id, str) and "Error" in wallet_set_id:
            raise ValueError(wallet_set_id)

        wallets_data = create_wallet(
            wallet_set_id=wallet_set_id,
            blockchains=req.blockchains,
            count=req.count
        )

        config_data = {
            "wallet_set_id": wallet_set_id,
            "wallets": wallets_data
        }

        save_config(config_data)
        return config_data

    except Exception as e:
        logger.exception("Treasury setup failed")
        raise HTTPException(status_code=500, detail=f"Failed to initialize treasury: {str(e)}")

@router.get("/config", response_model=SetupResponse)
async def get_treasury_config():
    config = load_config()
    if not config:
        raise HTTPException(status_code=404, detail="No treasury config found")
    return config

@router.post("/transfer", response_model=TransferResponse)
async def transfer(req: TransferRequest):
    """
    Transfer USDC between wallets.
    """
    config = load_config()
    if not config:
        raise HTTPException(status_code=404, detail="Treasury not initialized")

    result = transfer_tokens(
        source_wallet_id=req.source_wallet_id,
        destination_address=req.destination_address,
        amount=req.amount
    )

    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])

    return result
