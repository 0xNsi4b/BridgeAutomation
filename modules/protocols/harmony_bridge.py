from modules import Account
from eth_abi import abi
from utils.config import harmony, endpoint


class HarmonyBridge(Account):

    chains_available = list(harmony[0].keys())
    token = harmony

    def __init__(self, chain: str, private_key: str, proxy: str) -> None:
        super().__init__(chain=chain, private_key=private_key, proxy=proxy)
        self.contract = self.get_contract(harmony[0][self.chain], harmony[1])

    def get_fee(self, amount, tx_parameters, dst_chain_id):
        contract = self.get_contract(endpoint[0][self.chain], endpoint[1])

        types = ['bytes', 'uint256']
        values = [self.address.encode('utf-8'), amount]
        payload = abi.encode(types, values)

        return contract.functions.estimateFees(dst_chain_id,
                                               contract.address,
                                               payload,
                                               True,
                                               tx_parameters).call()[0]

    def bridge(self, amount, test=False):

        tx_parameters = '0x0001000000000000000000000000000000000000000000000000000000000007a120'

        lz_fee = self.get_fee(amount, tx_parameters, 116)
        transaction_dict = self.create_txn(amount + lz_fee)
        build_func = self.contract.functions.sendFrom(self.address,
                                                      116,
                                                      self.address,
                                                      amount,
                                                      self.address,
                                                      '0x0000000000000000000000000000000000000000',
                                                      tx_parameters).build_transaction(transaction_dict)
        signed_txn = self.sign_txn(build_func)
        if test:
            return signed_txn
        self.complete_transaction(signed_txn, 'Harmony bridge')
