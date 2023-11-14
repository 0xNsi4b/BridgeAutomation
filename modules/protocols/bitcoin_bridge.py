from modules import Account
from utils.config import bitcoinbridge, BTC


class BitcoinBridge(Account):

    chains_available = list(bitcoinbridge[0].keys())
    token = BTC

    def __init__(self, chain: str, private_key: str, proxy: str) -> None:
        super().__init__(chain=chain, private_key=private_key, proxy=proxy)

    def bridge(self, dst_chain_id, amount, test=False):

        contract = self.get_contract(bitcoinbridge[0][self.chain], bitcoinbridge[1])

        adapter_params = '0x000200000000000000000000000000000000000000000000000000000000000' \
                         '3d0900000000000000000000000000000000000000000000000000000000000000000' + self.address[2:]
        to_address = '0x000000000000000000000000' + self.address[2:]
        call_params = [self.address, '0x0000000000000000000000000000000000000000', adapter_params]

        lz_fee = contract.functions.estimateSendFee(dst_chain_id, to_address, amount, True, adapter_params).call()[0]

        transaction_dict = self.create_txn(lz_fee)

        build_func = contract.functions.sendFrom(self.address,
                                                 dst_chain_id,
                                                 to_address,
                                                 amount,
                                                 amount,
                                                 call_params).build_transaction(transaction_dict)

        transaction_hash = self.sign_txn(build_func)
        if test:
            return transaction_hash
        self.complete_transaction(transaction_hash, 'Bitcoin bridge')
