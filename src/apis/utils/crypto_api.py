import requests

def get_coinmarketcap_data():
    url = "https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

    parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
  }
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": "API-KEY",
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    return data