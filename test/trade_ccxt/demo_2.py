import ccxt

# 初始化
bian_exchange = ccxt.binance({
    "timeout": 15000,
    "enableRateLimit": True,
    'urls': {
        'logo': 'https://user-images.githubusercontent.com/1294454/29604020-d5483cdc-87ee-11e7-94c7-d1a8d9169293.jpg',
        'test': {
            'fapiPublic': 'https://testnet.binancezhfuture.com/fapi/v1',
            'fapiPrivate': 'https://testnet.binancezhfuture.com/fapi/v1',
            'public': 'https://testnet.binancezh.vision/api/v3',
            'private': 'https://testnet.binancezh.vision/api/v3',
            'v3': 'https://testnet.binancezh.vision/api/v3',
            'v1': 'https://testnet.binancezh.vision/api/v1',
        },
        'api': {
            'wapi': 'https://api.binancezhzh.com/wapi/v3',
            'sapi': 'https://api.binancezh.com/sapi/v1',
            'fapiPublic': 'https://fapi.binancezh.com/fapi/v1',
            'fapiPrivate': 'https://fapi.binancezh.com/fapi/v1',
            'public': 'https://api.binancezh.com/api/v3',
            'private': 'https://api.binancezh.com/api/v3',
            'v3': 'https://api.binancezh.com/api/v3',
            'v1': 'https://api.binancezh.com/api/v1',
        },
        'www': 'https://www.binancezh.com',
        'referral': 'https://www.binancezh.com/?ref=10205187',
        'doc': [
            'https://binancezh-docs.github.io/apidocs/spot/en',
        ],
        'api_management': 'https://www.binancezh.com/en/usercenter/settings/api-management',
        'fees': 'https://www.binancezh.com/en/fee/schedule',
    }
})

bian_markets = bian_exchange.load_markets()
bian_exchange.fetch_balance()
print(bian_markets)

"""
'urls': {
                'logo': 'https://user-images.githubusercontent.com/1294454/29604020-d5483cdc-87ee-11e7-94c7-d1a8d9169293.jpg',
                'api': {
                    'wapi': 'https://api.binance.com/wapi/v3',
                    'sapi': 'https://api.binance.com/sapi/v1',
                    'fapiPublic': 'https://fapi.binance.com/fapi/v1',
                    'fapiPrivate': 'https://fapi.binance.com/fapi/v1',
                    'public': 'https://api.binance.com/api/v3',
                    'private': 'https://api.binance.com/api/v3',
                    'v3': 'https://api.binance.com/api/v3',
                    'v1': 'https://api.binance.com/api/v1',
                },
                'www': 'https://www.binance.com',
                'referral': 'https://www.binance.com/?ref=10205187',
                'doc': [
                    'https://binance-docs.github.io/apidocs/spot/en',
                ],
                'api_management': 'https://www.binance.com/en/usercenter/settings/api-management',
                'fees': 'https://www.binance.com/en/fee/schedule',
            },


"""
"""

{ 
   "server":"my_server_ip", 
   "server_port":25, 
   "local_address": "127.0.0.1", 
   "local_port":1080, 
   "password":"8888",
   "timeout":300, 
   "method":"aes-256-cfb", 
   "fast_open": false
}

"""