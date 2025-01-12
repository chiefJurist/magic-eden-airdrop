from solana.rpc.api import Client
from solders.pubkey import Pubkey
import base58

# Connect to Solana mainnet RPC
client = Client("https://api.mainnet-beta.solana.com")

# Decode the base58 string to bytes
decoded_key = base58.b58decode("MEisE1HzehtrDpAAT8PnLHjpSSkRYakotTuJRPjTpo8")

# Magic Eden Program ID
magiceden_program_id = Pubkey(decoded_key)  # Convert to Pubkey

# Fetch recent transactions related to Magic Eden
response = client.get_signatures_for_address(magiceden_program_id, limit=100)

# Check if the response contains results and process them
if response:
    print("Recent wallet addresses interacting with Magic Eden:")
    for tx in response:
        signature = tx.signature
        transaction = client.get_transaction(signature)
        if transaction['result']:
            for account in transaction['result']['transaction']['message']['accountKeys']:
                print(account)
else:
    print("No results found.")