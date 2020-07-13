import requests
import pandas as pd
from datetime import datetime

base_url = "https://api.binancezh.com/"


def get_ticker_24h(symbol):
    """
        24hr 价格变动情况
    """
    if symbol is None:
        url = base_url + 'api/v3/ticker/24hr'
    else:
        symbol.replace('_', '').upper()
        url = base_url + 'api/v3/ticker/24hr?symbol={}'.format(symbol.replace('_', '').upper())

    try:
        rep_obj = requests.get(url)
    except Exception as e:
        print("错误：", e)
        return

    if rep_obj.status_code == 200:
        rep_json = rep_obj.json()
        print(rep_json)
        raw_df = pd.DataFrame(9).set_index(0)

        ticker_df = pd.DataFrame()
        print(raw_df)
    else:
        print("状态码错误:", rep_obj.status_code)





def main():
    # symbol = 'btc_usdt'
    symbol = None
    get_ticker_24h(symbol)


if __name__ == '__main__':
    # main()
    a = {'a': 2}
    b = a
    print(a)
    print(b)