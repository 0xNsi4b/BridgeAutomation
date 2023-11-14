from eth_abi import abi
from modules import Account
from utils.config import STG, endpoint


class StargateToken(Account):
    token = STG
    chains_available = list(STG[0].keys())

    def __init__(self, chain: str, private_key: str, proxy: str) -> None:
        super().__init__(chain=chain, private_key=private_key, proxy=proxy)
        self.tx_parameters = '0x00010000000000000000000000000000000000000000000000000000000000014c08'
        self.contract = self.get_contract(STG[0][self.chain], STG[1])

    def get_fee(self, amount, dst_chain_id):
        contract = self.get_contract(endpoint[0][self.chain], endpoint[1])

        types = ['bytes', 'uint256']
        values = [self.address.encode('utf-8'), amount]
        payload = abi.encode(types, values)

        func = contract.functions.estimateFees
        return func(dst_chain_id, contract.address, payload, True, self.tx_parameters).call()[0]

    def bridge(self, dst_chain_id: str, amount: int, test: bool = False):
        value = self.get_fee(amount, dst_chain_id)
        transaction_dict = self.create_txn(value)
        build_func = self.contract.functions.sendTokens(dst_chain_id,
                                                        self.address,
                                                        amount,
                                                        '0x0000000000000000000000000000000000000000',
                                                        self.tx_parameters).build_transaction(transaction_dict)
        signed_txn = self.sign_txn(build_func)

        if test:
            return signed_txn
        self.complete_transaction(signed_txn, 'STG bridge')
