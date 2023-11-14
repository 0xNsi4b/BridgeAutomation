import random
from modules.protocols import Angle, BitcoinBridge, StargateToken, StargateFinance
from utils.config import lz_id
from utils.helpers import sleep


class Bridge:
    def __init__(self, private_key: str, proxy: str):
        self.private_key = private_key
        self.proxy = proxy
        self._bridge_modules = {
            'angle': Angle,
            'bitcoin_bridge': BitcoinBridge,
            'stargate_token': StargateToken,
            'stargate_finance': StargateFinance
        }

    def _create_bridge_modules(self, bridge: str, chains) -> dict:
        return {chain: self._bridge_modules[bridge](chain, self.private_key, self.proxy) for chain in chains}

    @staticmethod
    def check_token_balance(chains: list, token: tuple[dict, str]) -> tuple[str, int]:
        while True:
            for chain in chains:
                balance = chain.get_balance(token)
                if balance > 0:
                    return chain.chain, balance
                sleep()

    @staticmethod
    def _create_subsequence(subsequence: list, chains: list, num_transactions: int) -> list:

        for i in range(num_transactions - 1):
            chains_copy = chains.copy()
            chains_copy.remove(subsequence[-1])
            element = random.choice(chains_copy)
            subsequence.append(element)

        return subsequence

    def transfer(self, use_chains: list, bridge: str, swaps: tuple[int, int], finish=None, test=True):

        token = self._bridge_modules[bridge].token
        chains_available = list(set(use_chains) & set(self._bridge_modules[bridge].chains_available))
        quantity_swap = random.randint(swaps[0], swaps[1])
        chains_dict = self._create_bridge_modules(bridge, chains_available)

        from_chain, balance = self.check_token_balance(list(chains_dict.values()), token)

        if finish is not None and from_chain != finish:
            quantity_swap -= 1

        subsequence = self._create_subsequence([from_chain], chains_available, quantity_swap)

        if finish is not None and subsequence[-1] != finish:
            subsequence.append(finish)

        for i in range(len(subsequence) - 1):
            from_chain = subsequence[i]
            to_chain = subsequence[i + 1]
            chains_dict[from_chain].bridge(lz_id[to_chain], balance, test)
            sleep()
            from_chain, balance = self.check_token_balance([chains_dict[to_chain]], token)

    # chains_dict[from_chain].transfer(self.to, balance)

