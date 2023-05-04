
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from apis.utils.crypto_api import get_coinmarketcap_data

class CoinMarketCapData(APIView):
    def get(self, request):
        data = get_coinmarketcap_data()
        return Response(data)