from django.urls import path
from .views import CoinMarketCapData, CoinMarketView

urlpatterns = [
    path('coinmarketcap/', CoinMarketCapData.as_view()),
    path('coinprices/', CoinMarketView.as_view())
]