import logging
from apis.utils.crypto_api import get_coinmarketcap_data
from apis.utils.metals_api import get_metalprice_data

class ApiRoutines:
    log = logging.getLogger()

    def filter_data(self):
        self.log.debug("Filtering Data!")
        coin_market_data = get_coinmarketcap_data()
        metal_market_data = get_metalprice_data()
        btc_price = coin_market_data.get("data")[0].get("quote").get("USD").get("price")
        gold_price = 1/float(metal_market_data.get("rates").get("XAU"))
        gold_price = str(gold_price)
        price_dict = {"btc_price": btc_price,
                      "gold_price": gold_price}
        return price_dict