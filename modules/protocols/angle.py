from modules import Account
from utils.config import angle


class Angle(Account):

    chains_available = list(angle[0].keys())
    token = angle

    def __init__(self, chain: str, private_key: str, proxy: str) -> None:
        super().__init__(chain=chain, private_key=private_key, proxy=proxy)
        self.contract = self.get_contract(angle[0][self.chain], angle[1])

    def bridge(self, dst_chain_id, amount, test=False):

        adapter_params = '0x000100000000000000000000000000000000000000000000000000000000000493e0'
        lz_fee = self.contract.functions.estimateSendFee(dst_chain_id,
                                                         self.address,
                                                         amount, True,
                                                         adapter_params).call()[0]
        transaction_dict = self.create_txn(lz_fee)

        self.approve(self.contract, self.contract.address, amount)
        build_func = self.contract.functions.send(dst_chain_id,
                                                  self.address,
                                                  amount,
                                                  self.address,
                                                  '0x0000000000000000000000000000000000000000',
                                                  adapter_params).build_transaction(transaction_dict)

        signed_txn = self.sign_txn(build_func)
        if test:
            return signed_txn

        self.complete_transaction(signed_txn, 'Angle bridge')
