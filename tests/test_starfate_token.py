import unittest

from eth_account.datastructures import SignedTransaction
from modules import StargateToken
from utils.config import test_data, lz_id


class TestStargateToken(unittest.TestCase):
    def setUp(self):
        self.key = test_data.evm_private_keys.get_secret_value()
        self.proxy = test_data.proxy.get_secret_value()
        self.chains = StargateToken.chains_available

    def test_contracts(self):
        for chain in self.chains:
            chain_class = StargateToken(chain, self.key, self.proxy)
            self.assertEqual(
                str(chain_class.contract.find_functions_by_name('sendTokens')[0]),
                '<Function sendTokens(uint16,bytes,uint256,address,bytes)>')

    def test_arbitrum(self):
        chains_copy = self.chains.copy()
        chains_copy.remove('ARBITRUM')
        arbitrum_class = StargateToken('ARBITRUM', self.key, self.proxy)
        for chain in chains_copy:
            self.assertEqual(type(arbitrum_class.bridge(lz_id[chain], 69, True)), SignedTransaction)
