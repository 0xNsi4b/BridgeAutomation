from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

main_directory = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    evm_private_keys: SecretStr
    proxy: SecretStr
    aptos_address: SecretStr

    model_config = SettingsConfigDict(env_file=f'{main_directory}/.env', env_file_encoding='utf-8')


test_data = Settings()

with open(f'{main_directory}/user_data/private_keys.txt', 'r') as file:
    keys = [row.strip() for row in file]

with open(f'{main_directory}/user_data/proxy.txt', 'r') as file:
    proxies = [row.strip() for row in file]

with open(f'{main_directory}/user_data/deposit_addresses.txt', 'r') as file:
    deposit_addresses = [row.strip() for row in file]

with open(f'{main_directory}/user_data/aptos_addresses.txt', 'r') as file:
    aptos_addresses = [row.strip() for row in file]

lz_id = {
    'OPTIMISM': 111,
    'BSC': 102,
    'BASE': 184,
    'GNOSIS': 145,
    'POLYGON': 109,
    'FANTOM': 112,
    'CELO': 125,
    'ARBITRUM': 110,
    'AVAX': 106,
}

BTC = (
    {
        'OPTIMISM': '0x68f180fcCe6836688e9084f035309E29Bf0A2095',
        'ARBITRUM': '0x2297aEbD383787A160DD0d9F71508148769342E3',
        'AVAX': '0x152b9d0FdC40C096757F570A51E494bd4b943E50',
        'BSC': '0x2297aEbD383787A160DD0d9F71508148769342E3',
        'POLYGON': '0x86Bb63148d17d445Ed5398ef26Aa05Bf76dD5b59',
    },
    f'{main_directory}/abi/erc20_abi.json'
)

STG = (
    {
        'OPTIMISM': '0x296F55F8Fb28E498B858d0BcDA06D955B2Cb3f97',
        'BSC': '0xB0D502E938ed5f4df2E681fE6E419ff29631d62b',
        'BASE': '0xE3B53AF74a4BF62Ae5511055290838050bf764Df',
        'POLYGON': '0x2F6F07CDcf3588944Bf4C42aC74ff24bF56e7590',
        'FANTOM': '0x2F6F07CDcf3588944Bf4C42aC74ff24bF56e7590',
        'ARBITRUM': '0x6694340fc020c5E6B96567843da2df01b2CE1eb6',
        'AVAX': '0x2F6F07CDcf3588944Bf4C42aC74ff24bF56e7590'
    },
    f'{main_directory}/abi/stg.json'
)

USDC = (
    {
        'ARBITRUM': '0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8',
        'OPTIMISM': '0x0b2c639c533813f4aa9d7837caf62653d097ff85',
        'AVAX': '0xb97ef9ef8734c71904d8002f8b6bc66dd9c48a6e',
        'POLYGON': '0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174',
        'BASE': '0x4c80e24119cfb836cdf0a6b53dc23f04f7e652ca'
    },
    f'{main_directory}/abi/erc20_abi.json'
)

angle = (
    {
        'ARBITRUM': '0x16cd38b1B54E7abf307Cb2697E2D9321e843d5AA',
        'AVAX': '0x14C00080F97B9069ae3B4Eb506ee8a633f8F5434',
        'BSC': '0x16cd38b1B54E7abf307Cb2697E2D9321e843d5AA',
        'OPTIMISM': '0x16cd38b1B54E7abf307Cb2697E2D9321e843d5AA',
    },
    f'{main_directory}/abi/angle_bridge.json'
)

aptosbridge = (
    {
        'ARBITRUM': '0x1BAcC2205312534375c8d1801C27D28370656cFf',
        'AVAX': '0xA5972EeE0C9B5bBb89a5B16D1d65f94c9EF25166',
        'BSC': '0x2762409Baa1804D94D8c0bCFF8400B78Bf915D5B',
        'OPTIMISM': '0x86Bb63148d17d445Ed5398ef26Aa05Bf76dD5b59',
    },
    f'{main_directory}/abi/aptos_bridge.json'
)

bitcoinbridge = (
    {
        'ARBITRUM': '0x2297aEbD383787A160DD0d9F71508148769342E3',
        'AVAX': '0x2297aEbD383787A160DD0d9F71508148769342E3',
        'BSC': '0x2297aEbD383787A160DD0d9F71508148769342E3',
        'POLYGON': '0x86Bb63148d17d445Ed5398ef26Aa05Bf76dD5b59',
        'OPTIMISM': '0x68f180fcCe6836688e9084f035309E29Bf0A2095',
    },
    f'{main_directory}/abi/btc_bridge.json'
)

coredao_bridge = (
    {
        'ARBITRUM': '0x2297aEbD383787A160DD0d9F71508148769342E3',
        'AVAX': '0x2297aEbD383787A160DD0d9F71508148769342E3',
        'BSC': '0x2297aEbD383787A160DD0d9F71508148769342E3',
        'POLYGON': '0x86Bb63148d17d445Ed5398ef26Aa05Bf76dD5b59',
    },
    f'{main_directory}/abi/btc_bridge.json'
)

harmony = (
    {
        'BSC': '0x128AEdC7f41ffb82131215e1722D8366faaD0CD4',
    },
    f'{main_directory}/abi/harmony_bridge.json'
)

stargate_router = (
    {
        'ARBITRUM': '0x53Bf833A5d6c4ddA888F69c22C88C9f356a41614',
        'AVAX': '0x45A01E4e04F14f7A4a6702c74187c5F6222033cd',
        # 'BSC': '0x4a364f8c717cAAD9A442737Eb7b8A55cc6cf18D8',
        'OPTIMISM': '0xB0D502E938ed5f4df2E681fE6E419ff29631d62b',
        'POLYGON': '0x45A01E4e04F14f7A4a6702c74187c5F6222033cd',
        'BASE': '0x45f1a95a4d3f3836523f5c83673c797f4d4d263b'
    },
    f'{main_directory}/abi/stargate_router.json'
)

endpoint = (
    {
        'OPTIMISM': '0x3c2269811836af69497E5F486A85D7316753cf62',
        'BSC': '0x3c2269811836af69497E5F486A85D7316753cf62',
        'BASE': '0xb6319cC6c8c27A8F5dAF0dD3DF91EA35C4720dd7',
        'GNOSIS': '0x3c2269811836af69497E5F486A85D7316753cf62',
        'POLYGON': '0x3c2269811836af69497E5F486A85D7316753cf62',
        'CORE': '0x9740FF91F1985D8d2B71494aE1A2f723bb3Ed9E4',
        'FANTOM': '0xb6319cC6c8c27A8F5dAF0dD3DF91EA35C4720dd7',
        'CELO': '0x3A73033C0b1407574C76BdBAc67f126f6b4a9AA9',
        'ARBITRUM': '0x3c2269811836af69497E5F486A85D7316753cf62',
        'AVAX': '0x3c2269811836af69497E5F486A85D7316753cf62'
    },
    f'{main_directory}/abi/endpoint.json'
)


