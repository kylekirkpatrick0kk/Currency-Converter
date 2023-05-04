from django.urls import path
from .views import CoinMarketCapData

urlpatterns = [
    path('coinmarketcap/', CoinMarketCapData.as_view()),
]