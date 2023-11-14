from modules import Account
from utils.config import aptosbridge


class AptosBridge(Account):

    chains_available = list(aptosbridge[0].keys())

    def __init__(self, chain: str, private_key: str, proxy: str) -> None:
        super().__init__(chain=chain, private_key=private_key, proxy=proxy)
        self.contract = self.get_contract(aptosbridge[0][self.chain], aptosbridge[1])

    def bridge(self, amount, aptos_address, test=False):
        adapter_params = '0x0002000000000000000000000000000000000000000000000000000000000000' \
                         '27100000000000000000000000000000000000000000000000000000000000000000' + aptos_address[2:]

        call_param = [self.address, '0x0000000000000000000000000000000000000000']

        lz_fee = self.contract.functions.quoteForSend(call_param,
                                                      adapter_params).call()[0]

        transaction_dict = self.create_txn(amount + lz_fee)

        build_func = self.contract.functions.sendETHToAptos(aptos_address,
                                                            amount,
                                                            [self.address,
                                                             '0x0000000000000000000000000000000000000000'],
                                                            adapter_params).build_transaction(transaction_dict)

        signed_txn = self.sign_txn(build_func)
        if test:
            return signed_txn

        self.complete_transaction(signed_txn, 'Aptos bridge')
