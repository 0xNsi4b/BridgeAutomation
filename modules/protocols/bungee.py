from modules import Account
# from utils.config import bungee


class Bungee(Account):
    # chains_available = list(bungee[0].keys())

    def __init__(self, chain: str, private_key: str, proxy: str) -> None:
        super().__init__(chain=chain, private_key=private_key, proxy=proxy)

    # def bridge(self, dst_chain_id,  amount):
    #     contract = bungee[0][chain].get_contract()
    #     transaction_dict = self.create_txn(amount)
    #     func = contract.functions.depositNativeToken(dst_chain_id, self.address).build_transaction(transaction_dict)
    #
    #     transaction_hash = self.complete_txn(build_func)
    #     self.wait_transaction(transaction_hash, 'Harmony bridge')
