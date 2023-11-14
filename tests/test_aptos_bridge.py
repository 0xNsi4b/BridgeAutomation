import unittest
from eth_account.datastructures import SignedTransaction
from modules import AptosBridge
from utils.config import test_data


class TestAptosBridge(unittest.TestCase):
    def setUp(self):
        self.key = test_data.evm_private_keys.get_secret_value()
        self.proxy = test_data.proxy.get_secret_value()
        self.aptos_address = test_data.aptos_address.get_secret_value()
        self.chains = AptosBridge.chains_available

    def test_contracts(self):
        for chain in self.chains:
            chain_class = AptosBridge(chain, self.key, self.proxy)
            self.assertEqual(
                str(chain_class.contract.find_functions_by_name('quoteForSend')[0]),
                '<Function quoteForSend((address,address),bytes)>')
            self.assertEqual(
                str(chain_class.contract.find_functions_by_name('sendETHToAptos')[0]),
                '<Function sendETHToAptos(bytes32,uint256,(address,address),bytes)>')

    def test_arbitrum(self):
        arbitrum_class = AptosBridge('ARBITRUM', self.key, self.proxy)
        self.assertEqual(type(arbitrum_class.bridge(6969, self.aptos_address, True)), SignedTransaction)
