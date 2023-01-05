import contract
from pyteal import *
from beaker import *
from beaker.client import ApplicationClient, Network
from beaker.client.api_providers import AlgoNode
import os
from dotenv import load_dotenv
from algosdk.atomic_transaction_composer import AccountTransactionSigner
from algosdk import mnemonic
from algosdk.encoding import decode_address


def call_method(app):
    load_dotenv()

    PASSPHRASE = os.environ.get("PASSPHRASE")

    # Open the file where we're saving the app ID
    text_file = open("./artifacts/app_id", "r")
    app_id = int(text_file.read())
    text_file.close()

    # Get the accounts trough the sandbox client
    user = AccountTransactionSigner(mnemonic.to_private_key(PASSPHRASE))

    # Create the Application Client
    app_client = ApplicationClient(
        client=AlgoNode(Network.TestNet).algod(),
        app=contract.AssetApplication(version=8),
        app_id=app_id,
        signer=user,

    )

    ## Call a method
    # app_client.opt_in()

    #result = app_client.call(contract.AssetApplication.add_asset, name="Certificado 2022",
    #                         checksum="fkdjfkdjfkdjfkdjfkadjfk",
    #                         idAsset="3BZLY5U2OK2NFJ4I2MFYH2BMIP4HPRKUHTNQCAVZHIXACGXHYWNNMEKP4I",
    #                         boxes=[(app_id, "3BZLY5U2OK2NFJ4I2MFYH2BMIP4HPRKUHTNQCAVZHIXACGXHYWNNMEKP4I")], )

    result = app_client.call(contract.AssetApplication.get_asset,  idAsset="3BZLY5U2OK2NFJ4I2MFYH2BMIP4HPRKUHTNQCAVZHIXACGXHYWNNMEKP4I", boxes=[(app_id, "3BZLY5U2OK2NFJ4I2MFYH2BMIP4HPRKUHTNQCAVZHIXACGXHYWNNMEKP4I")],)

    app.logger.info("result ---- >>>")
    app.logger.info(repr(result))
    app.logger.info(result.tx_info)

    # app_client.close_out()
    return {"tx_info": result.tx_info, "tx_id": result.tx_id, "return_value": result.return_value}
