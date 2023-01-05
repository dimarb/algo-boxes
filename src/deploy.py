import contract
from pyteal import *
import os
from dotenv import load_dotenv
from beaker.client import ApplicationClient, Network
from beaker.client.api_providers import AlgoNode
from algosdk import account
from algosdk import mnemonic
from algosdk.atomic_transaction_composer import AccountTransactionSigner


def deploy():
    load_dotenv()

    PASSPHRASE = os.environ.get("PASSPHRASE")

    # Compiling the contract
    contract.AssetApplication().dump("artifacts")

    # with something like ``AlgoNode(Network.TestNet).algod()``

    user = AccountTransactionSigner(mnemonic.to_private_key(PASSPHRASE))
    print(user.__dict__)
    user_address = account.address_from_private_key(user.private_key)
    print(user_address)

    app_client = ApplicationClient(
        client=AlgoNode(Network.TestNet).algod(),
        app=contract.AssetApplication(version=8),
        signer=user,
        sender=user_address,
    )
    # Creates the smart contract on-chain
    app_id, app_addr, txid = app_client.create()

    # Saves the app ID on a file to use it later
    open("./artifacts/app_id", "w").write(str(app_id))

    return {"txid":txid, "app_id":app_id, "app_addr": app_addr}
