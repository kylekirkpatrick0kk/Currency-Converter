import logging
from apis.utils.crypto_api import get_coinmarketcap_data
from apis.utils.metals_api import get_metalprice_data

class ApiRoutines:
    log = logging.getLogger()

    def filter_data(self):
        self.log.debug("Filtering Data!")
        data = get_coinmarketcap_data()
        #data = get_metalprice_data()
        btc_price = data.get("data")[0].get("quote").get("USD").get("price")
        price_dict = {"btc_price": btc_price}
        return price_dict