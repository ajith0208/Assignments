
# 4. The below API print the price of Bitcoin in USD and GBP
# https://api.coindesk.com/v1/bpi/currentprice.json
# • Collect data from this API for 1 day at 5 minutes interval. I.e you will have at least
# 288 unique data points. Consecutive data points should not have same value.
# • Find the highest and lowest price of bitcoin from the collected data, without using minimum
# or maximum functions
import time
import pandas as pd
import requests as requests

api = 'https://api.coindesk.com/v1/bpi/currentprice.json'

final_data = {'year': [],
              'month': [],
              'day': [],
              'time': [],
              'chartName': [],
              'USD ($)': [],
              'GBP (£)': [],
              'EUR (€)': [],
              }
while True:
    response = requests.get(api)
    data = response.json()
    final_data['year'].append(data['time']['updated'].split()[2])
    final_data['month'].append(data['time']['updated'].split()[0])
    final_data['day'].append(data['time']['updated'].split()[1][:-1])
    final_data['time'].append(data['time']['updated'].split()[3])
    final_data['chartName'].append(data['chartName'])
    final_data['USD ($)'].append(data['bpi']['USD']['rate'])
    final_data['GBP (£)'].append(data['bpi']['GBP']['rate'])
    final_data['EUR (€)'].append(data['bpi']['EUR']['rate'])
    df = pd.DataFrame.from_dict(final_data)
    df.to_csv('data.csv')
    time.sleep(300)
    if final_data['day'] == '16' and final_data['time'] == final_data['time'][0]:
        break

