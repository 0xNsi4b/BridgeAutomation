import unittest

from eth_account.datastructures import SignedTransaction
from modules import StargateFinance
from utils.config import test_data, lz_id


class TestStargateFinance(unittest.TestCase):
    def setUp(self):
        self.key = test_data.evm_private_keys.get_secret_value()
        self.proxy = test_data.proxy.get_secret_value()
        self.chains = StargateFinance.chains_available

    def test_contracts(self):
        for chain in self.chains:
            chain_class = StargateFinance(chain, self.key, self.proxy)
            self.assertEqual(
                str(chain_class.contract.find_functions_by_name('quoteLayerZeroFee')[0]),
                '<Function quoteLayerZeroFee(uint16,uint8,bytes,bytes,(uint256,uint256,bytes))>')
            self.assertEqual(
                str(chain_class.contract.find_functions_by_name('swap')[0]),
                '<Function swap(uint16,uint256,uint256,address,uint256,uint256,(uint256,uint256,bytes),bytes,bytes)>')

    def test_arbitrum(self):
        chains_copy = self.chains.copy()
        chains_copy.remove('ARBITRUM')
        arbitrum_class = StargateFinance('ARBITRUM', self.key, self.proxy)
        for chain in chains_copy:
            self.assertEqual(type(arbitrum_class.bridge(lz_id[chain], 69, True)), SignedTransaction)
