import unittest
from eth_account.datastructures import SignedTransaction
from modules import HarmonyBridge, Bridge
from utils.config import test_data


class TestHarmonyBridge(unittest.TestCase):
    def setUp(self):
        self.key = test_data.evm_private_keys.get_secret_value()
        self.proxy = test_data.proxy.get_secret_value()
        self.chains = HarmonyBridge.chains_available

    def test_stargate_token(self):
        use_bridge = 'stargate_token'
        use_chains = ['ARBITRUM', 'OPTIMISM']
        finish = 'OPTIMISM'
        swaps = (2, 2)
        Bridge(self.key, self.proxy).transfer(use_chains, use_bridge, swaps, finish, test=True)
