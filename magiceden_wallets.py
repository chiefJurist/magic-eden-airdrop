from solana.rpc.api import Client
from solders.pubkey import Pubkey
import base58

# Connect to Solana mainnet RPC
client = Client("https://api.mainnet-beta.solana.com")

# Decode the base58 string to bytes
decoded_key = base58.b58decode("MEisE1HzehtrDpAAT8PnLHjpSSkRYakotTuJRPjTpo8")

# Magic Eden Program ID
magiceden_program_id = Pubkey(decoded_key)  # Convert to Pubkey

# Set to store unique wallet addresses
unique_wallets = set()

# Initial call to get the first batch of signatures
response = client.get_signatures_for_address(magiceden_program_id, limit=100)

# Print the response to inspect its structure
print(response)

# Assuming response is a GetSignaturesForAddressResp object, check the attributes
if hasattr(response, 'result'):
    # Loop through the response to fetch all signatures
    while response.result:
        for tx in response.result:
            if tx.err is None:  # Successful transaction (no error)
                signature = tx.signature
                # Fetch the transaction details
                transaction = client.get_transaction(signature)
                if transaction['result']:
                    # Extract the account keys from the transaction
                    for account in transaction['result']['transaction']['message']['accountKeys']:
                        unique_wallets.add(account)  # Add account to the set of unique wallets

        # If there are more results, paginate and fetch the next batch
        if hasattr(response, 'meta') and 'next' in response.meta:
            response = client.get_signatures_for_address(magiceden_program_id, before=response.meta['next'], limit=100)
        else:
            break

# Display all unique wallet addresses
print("Wallet addresses that have interacted with Magic Eden:")
for wallet in unique_wallets:
    print(wallet)
