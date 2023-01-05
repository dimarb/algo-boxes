from pyteal import *
from beaker import *
from beaker.lib.storage import Mapping, List

# Use a box per member to denote membership parameters
class AssetsObject(abi.NamedTuple):
    name: abi.Field[abi.String]
    checksum: abi.Field[abi.String]


# Create a class, subclassing Application from beaker
class AssetApplication(Application):

  assets = Mapping(abi.String, AssetsObject)

  @external(authorize=Authorize.only(Global.creator_address()))
  def add_asset(self, name: abi.String, idAsset : abi.String, checksum : abi.String  ):

    return Seq(
        (asset := AssetsObject()).set(name, checksum),
        self.assets[idAsset.get()].set(asset),
        Approve()
    )

  @external(authorize=Authorize.only(Global.creator_address()))
  def get_asset(self, idAsset : abi.String, * , output: abi.String ):
      return output.set(self.assets[idAsset.get()].get())


  @opt_in
  def opt_in(self):
      return Approve()
