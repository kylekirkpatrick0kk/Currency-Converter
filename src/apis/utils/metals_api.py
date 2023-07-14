import requests
from calc.settings import METAL_PRICE_API_SECRET

def get_metalprice_data():
    url = f"https://api.metalpriceapi.com/v1/latest?api_key={METAL_PRICE_API_SECRET}"
    

    response = requests.get(url)
    data = response.json()

    return data