from urllib.request import urlopen
import json

url = 'https://btc-e.com/api/2/btc_usd/ticker'
response = urlopen(url)
data = json.loads(response.read().decode())

tds = ['last', 'buy', 'sell', 'high', 'low', 'vol']
for t in tds:
    print(data['ticker'][t])
