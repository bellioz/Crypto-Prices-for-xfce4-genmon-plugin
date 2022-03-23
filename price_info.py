from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

ids = ['bitcoin', 'litecoin', 'ethereum', 'binancecoin']

try:
    coins_prices = cg.get_price(ids, vs_currencies='usd')

    print('BTC:', coins_prices['bitcoin']['usd'], '|',
          'BNB:', coins_prices['binancecoin']['usd'], ' ')
except Exception:
    print('CoinGecko | Нет данных')

'''
# Поиск монеты по названию в id
for item in cg.get_coins_list():
    if 'binance' in item['id']:
        print(item)
'''
