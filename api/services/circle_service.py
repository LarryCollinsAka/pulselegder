import uuid
from circle_developer_controlled_wallets.apis import WalletSetsApi, WalletsApi
from circle_developer_controlled_wallets.models import (
    CreateWalletSetRequest, 
    CreateWalletRequest
)
from circle_developer_controlled_wallets import ApiException
from core.config import settings
from .client import client # Assuming our initialized client is here

def create_wallet_set(name: str = "Pulse Ledger WalletSet"):
    api_instance = WalletSetsApi(client)
    try:
        request = CreateWalletSetRequest.from_dict({
            "name": name,
            "idempotencyKey": str(uuid.uuid4()),
            "entitySecretCiphertext": settings.CIRCLE_ENTITY_SECRET
        })
        response = api_instance.create_wallet_set(request)
        return response.data.wallet_set.id
    except ApiException as e:
        # Log the error and return a descriptive message for the UI
        print(f"Exception calling WalletSetsApi: {e}")
        return f"Error: {e.reason}"

def create_wallet(wallet_set_id: str, account_type: str = "SCA", blockchains: list = None, count: int = 1):
    # Flexible default for blockchains
    if blockchains is None:
        blockchains = ["MATIC-AMOY"]

    api_instance = WalletsApi(client)
    try:
        request = CreateWalletRequest.from_dict({
            "accountType": account_type,
            "blockchains": blockchains,
            "count": count,
            "walletSetId": wallet_set_id,
            "idempotencyKey": str(uuid.uuid4()),
            "entitySecretCiphertext": settings.CIRCLE_ENTITY_SECRET
        })
        response = api_instance.create_wallet(request)
        
        # Return rich metadata instead of just a string address
        return [{
            "id": w.id,
            "address": w.address,
            "blockchain": w.blockchain,
            "state": w.state,
            "createDate": w.create_date
        } for w in response.data.wallets]
        
    except ApiException as e:
        print(f"Exception calling WalletsApi: {e}")
        return []