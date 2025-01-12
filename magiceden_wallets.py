from solana.rpc.api import Client
from solders.pubkey import Pubkey
import base58

# Connect to Solana mainnet RPC
client = Client("https://api.mainnet-beta.solana.com")

# Decode the base58 string to bytes
decoded_key = base58.b58decode("MEisE1HzehtrDpAAT8PnLHjpSSkRYakotTuJRPjTpo8")

# Magic Eden Program ID
magiceden_program_id = Pubkey(decoded_key)  # Convert to Pubkey

# Initial call to get the first batch of signatures with limit 20
response = client.get_signatures_for_address(magiceden_program_id, limit=20)

# Print the entire response to inspect its structure
print("Full response:")
print(response)
