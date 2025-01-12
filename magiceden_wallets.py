from solana.rpc.api import Client
from solders.pubkey import Pubkey


# Connect to Solana mainnet RPC
client = Client("https://api.mainnet-beta.solana.com")

# Magic Eden Program ID
magiceden_program_id = PublicKey("MEisE1HzehtrDpAAT8PnLHjpSSkRYakotTuJRPjTpo8")  # Convert to Pubkey

# Fetch recent transactions related to Magic Eden
response = client.get_signatures_for_address(magiceden_program_id, limit=100)

print("Recent wallet addresses interacting with Magic Eden:")
for tx in response['result']:
    signature = tx['signature']
    transaction = client.get_transaction(signature)
    if transaction['result']:
        for account in transaction['result']['transaction']['message']['accountKeys']:
            print(account)