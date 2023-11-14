from random import random

from modules import Account


class Woofi(Account):

    tokens_available = ['USDC']

    def __init__(self, chain: str, private_key: str, proxy: str) -> None:
        super().__init__(chain=chain, private_key=private_key, proxy=proxy)

    def bridge(self, dst_chain_id, amount):
        contract = self.woo_crosschain_contract

        ref_id = random.randint(10000000000000000, 90000000000000000)

        src_infos = [self.USDC_address, self.USDC_address, amount, amount]

        dst_infos = [dst_chain_id, usdc_address, usdc_address, int(amount * 0.99), 0]

        lz_fee = contract.functions.quoteLayerZeroFee(ref_id, self.address, src_infos, dst_infos).call()[0]

        transaction_dict = self.create_txn(lz_fee)

        build_func = contract.functions.crossSwap(ref_id,
                                                  self.address,
                                                  src_infos,
                                                  dst_infos).build_transaction(transaction_dict)

        transaction_hash = self.sign_txn(build_func)
        self.complete_transaction(transaction_hash, 'Woofi bridge')
