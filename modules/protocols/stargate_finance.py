from modules import Account
from utils.config import stargate_router, USDC


class StargateFinance(Account):
    chains_available = list(stargate_router[0].keys())
    token = USDC

    def __init__(self, chain: str, private_key: str, proxy: str) -> None:
        super().__init__(chain=chain, private_key=private_key, proxy=proxy)
        self.contract = self.get_contract(stargate_router[0][self.chain], stargate_router[1])

    def bridge(self, dst_chain_id, amount, test=False):
        source_pool_id = 1
        dest_pool_id = 1
        refund_address = self.address
        amount_out_min = int(amount * 0.995)
        lz_tx_odj = [0, 0, '0x0000000000000000000000000000000000000001']
        to = self.address
        data = '0x'

        value = self.contract.functions.quoteLayerZeroFee(dst_chain_id,
                                                          source_pool_id,
                                                          '0x0000000000000000000000000000000000000001',
                                                          '0x',
                                                          lz_tx_odj).call()[0]

        transaction_dict = self.create_txn(value)

        self.approve(self.get_contract(USDC[0][self.chain], USDC[1]), self.contract.address, amount)

        build_func = self.contract.functions.swap(dst_chain_id,
                                                  source_pool_id,
                                                  dest_pool_id,
                                                  refund_address,
                                                  amount,
                                                  amount_out_min,
                                                  lz_tx_odj,
                                                  to,
                                                  data).build_transaction(transaction_dict)
        signed_txn = self.sign_txn(build_func)

        if test:
            return signed_txn
        self.complete_transaction(signed_txn, f'StargateFinance USDC bridge')
