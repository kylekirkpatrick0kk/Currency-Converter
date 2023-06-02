
import logging

from typing import Any
from django.shortcuts import render

from rest_framework.views import View, APIView
from rest_framework.response import Response

from .routines import ApiRoutines


class CoinMarketCapData(APIView):
    def __init__(self, **kwargs: Any) -> None:
        self.log = logging.getLogger(f"{__name__}.CoinMarketCapData")
    
    def get(self, request):
        self.log.debug("Get request from CoinMarketCapData API View.")
        filtered_response = ApiRoutines().filter_data()
        return Response(filtered_response)
    

class CoinMarketView(View):
    def get(self, request):
        return render(request, "index.html")