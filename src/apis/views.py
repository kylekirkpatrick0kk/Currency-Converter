
import logging

from typing import Any
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from apis.utils.crypto_api import get_coinmarketcap_data

class CoinMarketCapData(APIView):
    def __init__(self, **kwargs: Any) -> None:
        self.log = logging.getLogger(f"{__name__}.CoinMarketCapData")
    
    def get(self, request):
        data = get_coinmarketcap_data()
        self.log.debug("Get request from CoinMarketCapData API View.")
        return Response(data)