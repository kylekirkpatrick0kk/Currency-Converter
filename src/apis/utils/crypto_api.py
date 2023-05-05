import requests
from calc.settings import API_SECRET

def get_coinmarketcap_data():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

    parameters = {
  'start':'1',
  'limit':'20',
  'convert':'USD'
  }
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": API_SECRET,
    }

    response = requests.get(url, headers=headers, params=parameters)
    data = response.json()

    return data