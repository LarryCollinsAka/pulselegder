import uuid
from circle_developer_controlled_wallets.apis import WalletSetsApi, WalletsApi, TransactionsApi
from circle_developer_controlled_wallets.models import (
    CreateWalletSetRequest,
    CreateWalletRequest,
    CreateTransactionRequest
)
from circle_developer_controlled_wallets import ApiException
from core.config import settings
from .client import client  # Initialized client

# -----------------------------
# Wallet Set Creation
# -----------------------------
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
        print(f"Exception calling WalletSetsApi: {e}")
        return f"Error: {e.reason}"

# -----------------------------
# Wallet Creation
# -----------------------------
def create_wallet(wallet_set_id: str, account_type: str = "SCA", blockchains: list = None, count: int = 1):
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

# -----------------------------
# Token Transfer
# -----------------------------
def transfer_tokens(source_wallet_id: str, destination_address: str, amount: int, blockchain: str = "MATIC-AMOY"):
    """
    Transfer USDC between wallets.
    amount is in base units (e.g. 1000000 = 1 USDC).
    """
    api_instance = TransactionsApi(client)
    try:
        request = CreateTransactionRequest.from_dict({
            "idempotencyKey": str(uuid.uuid4()),
            "source": {
                "walletId": source_wallet_id
            },
            "destination": {
                "address": destination_address,
                "blockchain": blockchain
            },
            "amounts": [str(amount)],
            "tokenId": "USDC"
        })
        response = api_instance.create_transaction(request)
        tx = response.data.transaction
        return {
            "transactionId": tx.id,
            "hash": tx.tx_hash,
            "status": tx.state
        }
    except ApiException as e:
        print(f"Exception calling TransactionsApi: {e}")
        return {"error": str(e)}
