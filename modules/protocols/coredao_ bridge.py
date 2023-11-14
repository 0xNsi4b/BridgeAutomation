from modules import Account


class CoredaoBridge(Account):

    chains_available = coredao_bridge[0].keys()

    def __init__(self, chain: str, private_key: str, proxy: str) -> None:
        super().__init__(chain=chain, private_key=private_key, proxy=proxy)

    # def coredao_bridge(self, amount):
    #     contract = self.get_contract(coredao_bridge[0][self.chain], coredao_bridge[1])
    #
    #     call_parameters = [self.address, '0x0000000000000000000000000000000000000000']
    #
    #     lz_fee = contract.functions.estimateBridgeFee(True, '0x').call()[0]
    #     transaction_dict = self.create_txn(lz_fee)
    #
    #     build_func = contract.functions.bridge(self.USDC_address,
    #                                            amount,
    #                                            self.address,
    #                                            call_parameters,
    #                                            '0x').build_transaction(transaction_dict)
    #
    #
    #     transaction_hash = self.complete_txn(build_func)
    #     self.wait_transaction(transaction_hash, 'Coredao bridge')
