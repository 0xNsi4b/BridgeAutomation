from modules import Account


class TestnetBridge(Account):

    chains_available = ['ARBITRUM', 'BASE']

    def __init__(self, chain: str, private_key: str, proxy: str) -> None:
        super().__init__(chain=chain, private_key=private_key, proxy=proxy)

    # def bridge(self, amount):
    #     # Uniswap Quoter
    #     token_in = '0x82aF49447D8a07e3bd95BD0d56f35241523fBab1'
    #     token_out = '0xdD69DB25F6D620A7baD3023c5d32761D353D3De9'
    #     fee = 500
    #
    #     price = self.uniswap_contract.functions.quoteExactInputSingle(token_in,
    #                                                                   token_out,
    #                                                                   fee,
    #                                                                   amount,
    #                                                                   0).call()
    #
    #     lz_tx_odj = [0, 0, '0x0000000000000000000000000000000000000000']
    #     lz_fee = self.router_contract.functions.quoteLayerZeroFee(110,
    #                                                               1,
    #                                                               '0x0000000000000000000000000000000000000000',
    #                                                               '0x',
    #                                                               lz_tx_odj).call()[0]
    #
    #     amount_out_min = int(price * 0.95)
    #
    #     transaction_dict = self.create_txn(amount + lz_fee)
    #     build_func = self.testnet_contract.functions.swapAndBridge(amount,
    #                                                                amount_out_min,
    #                                                                154,
    #                                                                self.address,
    #                                                                self.address,
    #                                                                '0x0000000000000000000000000000000000000000',
    #                                                                '0x').build_transaction(transaction_dict)
    #     # gas = 2500000
    #
    #     transaction_hash = self.complete_txn(build_func)
    #     self.wait_transaction(transaction_hash, 'Testnet bridge')
