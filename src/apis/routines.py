import logging
from apis.utils.crypto_api import get_coinmarketcap_data

class ApiRoutines:
    log = logging.getLogger()

    def filter_data(self):
        self.log.debug("Filtering Data!")
        data = get_coinmarketcap_data()
        return data