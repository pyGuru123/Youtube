#							Realtime currency converter

# service used : alpha vantage api

import requests

api_key = '21XTTGBDL2CBO627'

from_c = 'USD'
to_c = 'INR'

amount = 50

base_url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE'
main_url = base_url + '&from_currency=' + from_c + '&to_currency=' + to_c + '&apikey=' + api_key

response = requests.get(main_url)
result = response.json()

key = result['Realtime Currency Exchange Rate']
rate = key['5. Exchange Rate']

print('Realtime exchange rate')
print(f'1 {from_c} : {rate} {to_c}')

print()

print('Converted amount')
print(f'{amount} {from_c} : {float(rate) * amount} {to_c}')