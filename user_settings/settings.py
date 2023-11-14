rpc = {
    'ETH': {'explorer': 'https://eth.llamarpc.com',
            'rpc': 'https://eth.llamarpc.com'
            },
    'OPTIMISM': {'explorer': 'https://optimistic.etherscan.io/tx/',
                 'rpc': 'https://1rpc.io/op'
                 },

    'ARBITRUM': {'explorer': 'https://arbiscan.io/tx/',
                 'rpc': 'https://arb-mainnet.g.alchemy.com/v2/-wpQCRLzVCXln9FpId1qZKFOglWej9Fd'
                 },

    'AVAX': {'explorer': 'https://snowtrace.io/tx/',
             'rpc': 'https://avalanche.blockpi.network/v1/rpc/public',
             },

    'BASE': {'explorer': 'https://basescan.org/tx/',
             'rpc': 'https://base.meowrpc.com'
             },

    'FANTOM': {'explorer': 'https://ftmscan.com/tx/',
               'rpc': 'https://rpc.fantom.network',
               },

    'POLYGON': {'explorer': 'https://polygonscan.com/tx/',
                'rpc': 'https://polygon-bor.publicnode.com',
                },

    'BSC': {'explorer': 'https://bscscan.com/tx/',
            'rpc': 'https://rpc.ankr.com/bsc',
            },

    'GNOSIS': {'explorer': 'https://gnosisscan.io/tx/',
               'rpc': 'https://gnosis.blockpi.network/v1/rpc/public',
               },

    'CELO': {'explorer': 'https://celoscan.io/tx/',
             'rpc': 'https://forno.celo.org',
             },

    'CORE': {'explorer': 'https://scan.coredao.org/tx/',
             'rpc': 'https://rpc.coredao.org',
             }
}


random_wallet = True

sleep_min = 20
sleep_max = 30

# PROXY MODE
proxy = False

max_workers = 1

# GWEI CONTROL MODEm
max_gwei = 80
