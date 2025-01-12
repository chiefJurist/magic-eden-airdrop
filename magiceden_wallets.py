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

# Set to store unique wallet addresses
unique_wallets = set()

# Loop through the results and filter only successful transactions
if hasattr(response, 'result'):
    for tx in response.result:
        if tx.err is None:  # Successful transaction (no error)
            signature = tx.signature
            # Fetch the transaction details
            transaction = client.get_transaction(signature)
            if transaction['result']:
                # Extract the account keys from the transaction
                for account in transaction['result']['transaction']['message']['accountKeys']:
                    unique_wallets.add(account)  # Add account to the set of unique wallets

# Display all unique wallet addresses
print("Wallet addresses that have interacted with Magic Eden:")
for wallet in unique_wallets:
    print(wallet)
