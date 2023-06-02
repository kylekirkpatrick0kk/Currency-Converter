import requests
from calc.settings import PRO_COIN_API_SECRET

def get_coinmarketcap_data():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

    parameters = {
      'start':'1',
      'limit':'3',
      'convert':'USD'
    }
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": PRO_COIN_API_SECRET,
    }

    response = requests.get(url, headers=headers, params=parameters)
    data = response.json()
    return data