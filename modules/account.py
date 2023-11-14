import json
import time
import random

from loguru import logger
from web3 import Web3
from eth_account import Account as EthereumAccount
from web3.exceptions import TransactionNotFound

from user_settings.settings import rpc, max_gwei
from utils.config import STG
from utils.helpers import sleep
from web3.contract import Contract


class Account:
    def __init__(self, chain: str, private_key: str, proxy: str) -> None:
        self.chain = chain
        self.private_key = private_key
        self._explorer = rpc[self.chain]['explorer']
        self.logger = logger

        self._request_kwargs = {}
        self.proxy_api = {}

        if proxy:
            proxy_split = proxy.split(':')
            proxy = f'{proxy_split[2]}:{proxy_split[3]}@{proxy_split[0]}:{proxy_split[1]}'
            self.proxy_api = {
                'http': f'http://{proxy}',
                'https': f'http://{proxy}'}
            self._request_kwargs = {
                'proxies': {'https': f'http://{proxy}'}}

        self.w3 = Web3(Web3.HTTPProvider(rpc[self.chain]['rpc'], request_kwargs=self._request_kwargs))
        self.account = EthereumAccount.from_key(private_key)
        self.address = self.account.address

    def create_txn(self, value=0) -> dict:
        return {
            'chainId': self.w3.eth.chain_id,
            'from': self.address,
            'value': value,
            # 'gas': self.w3.eth.gas_price,
            'nonce': self.w3.eth.get_transaction_count(self.address)
        }

    def check_gas(self):
        w3 = Web3(Web3.HTTPProvider(rpc['ETH']['rpc'], request_kwargs=self._request_kwargs))
        while True:
            gas_price = w3.from_wei(w3.eth.gas_price, 'gwei')
            if gas_price > max_gwei:
                logger.info(f'Current gas price: {int(gas_price)} > {int(max_gwei)}')
                sleep()
            else:
                logger.success(f'Current gas price is normal: {int(gas_price)} < {int(max_gwei)}')
                break

    def sign_txn(self, txn):
        signed_txn = self.w3.eth.account.sign_transaction(txn, self.private_key)
        return signed_txn

    def get_balance(self, token: tuple) -> dict:
        contract = self.get_contract(token[0][self.chain], token[1])
        return contract.functions.balanceOf(self.address).call()

    def get_contract(self, address, file_name) -> Contract:
        with open(file_name) as file:
            abi = json.load(file)
        return self.w3.eth.contract(address=Web3.to_checksum_address(address),
                                    abi=abi)

    def transfer(self, to: str, amount: int):
        contract = self.get_contract(STG[0][self.chain], STG[1])
        func = contract.functions.transfer(
            Web3.to_checksum_address(to),
            amount
        ).build_transaction(self.create_txn())
        self._transaction(self.sign_txn(func), 'send')

    def approve(self, token_contract: Contract, spender_address: str, amount: float):
        allowance_amount = token_contract.functions.allowance(self.address, spender_address).call()

        if amount > allowance_amount:
            func = token_contract.functions.approve(
                spender_address,
                2 ** 256 - 1
            ).build_transaction(self.create_txn())

            self.complete_transaction(self.sign_txn(func),
                                  f'{token_contract.functions.symbol().call()} approve')
            time.sleep(random.randint(15, 30))

    def complete_transaction(self, signed_txn: any, name: str = '', timeout: int = 120):
        self.check_gas()
        transaction_hash = self.w3.to_hex(self.w3.eth.send_raw_transaction(signed_txn.rawTransaction))

        start_time = time.time()
        while True:
            try:
                receipts = self.w3.eth.get_transaction_receipt(transaction_hash)
                status = receipts.get('status')
                if status == 1:
                    self.logger.success(f'{self.address} {name}: {self._explorer}{transaction_hash}')
                    return True
                elif status is None:
                    time.sleep(0.3)
                else:
                    self.logger.error(f'{self.address} {name}: {self._explorer}{transaction_hash} transaction failed!')
                    return False
            except TransactionNotFound:
                if time.time() - start_time > timeout:
                    self.logger.error(f'{self.address}: {transaction_hash} transaction not found!')
                    return False
                time.sleep(1)
