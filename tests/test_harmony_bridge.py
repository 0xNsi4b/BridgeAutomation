import unittest
from eth_account.datastructures import SignedTransaction
from modules import HarmonyBridge
from utils.config import test_data


class TestHarmonyBridge(unittest.TestCase):
    def setUp(self):
        self.key = test_data.evm_private_keys.get_secret_value()
        self.proxy = test_data.proxy.get_secret_value()
        self.chains = HarmonyBridge.chains_available

    def test_contracts(self):
        for chain in self.chains:
            chain_class = HarmonyBridge(chain, self.key, self.proxy)
            self.assertEqual(
                str(chain_class.contract.find_functions_by_name('sendFrom')[0]),
                '<Function sendFrom(address,uint16,bytes,uint256,address,address,bytes)>')

    def test_arbitrum(self):
        arbitrum_class = HarmonyBridge('BSC', self.key, self.proxy)
        self.assertEqual(type(arbitrum_class.bridge(6969,  True)), SignedTransaction)
