from modules import *
from utils.helpers import get_percent


def random_transfers(data):
    """
    Список мостов: angle, bitcoin_bridge, stargate_finance
    swaps - количества транзакций
    use_chains - список сетей из которых софт будет рандомно выбирать при бридже
    Софт автоматически проверяет доступна ли сеть
    """

    use_bridge = 'bitcoin_bridge'
    use_chains = ['ARBITRUM', 'OPTIMISM']
    use_token = 'BTC'
    finish = None

    swaps = (4, 6)

    Bridge(data[0], data[1])\
        .transfer(use_chains, use_bridge, swaps, finish=finish, token_name=use_token)


def galaxy_stargate_week1(data):
    """
    Список мостов: angle, bitcoin_bridge, stargate_finance
    swaps - количества транзакций
    use_chains - список токенов, из которых софт будет рандомно выбирать при свапе
    Софт автоматически проверяет доступна ли сеть
    """

    use_bridge = 'stargate_finance'
    use_chains = ['ARBITRUM', 'BASE']
    finish = 'OPTIMISM'

    swaps = (2, 2)

    Bridge(data[0], data[1])\
        .transfer(use_chains, use_bridge, swaps, finish)


def aptos_bridge(data):
    min_percent = 1
    max_percent = 2
    chain = 'ARBITRUM'
    
    # not change this
    a_bridge = AptosBridge(chain, data[0], data[1])
    amount = int(a_bridge.w3.eth.get_balance(a_bridge.address) * get_percent(min_percent, max_percent))
    a_bridge.bridge(amount, data[2])


def harmony_bridge(data):
    min_percent = 1
    max_percent = 2
    chain = 'BSC'

    # not change this
    h_bridge = HarmonyBridge(chain, data[0], data[1])
    amount = int(h_bridge.w3.eth.get_balance(h_bridge.address) * get_percent(min_percent, max_percent))
    h_bridge.bridge(amount)
