from django.shortcuts import render
import yfinance as yf

from .models import HisseSenedi

def ana_sayfa(request):
    hisse_listesi = HisseSenedi.objects.all()
    
    for hisse in hisse_listesi:
        stock = yf.Ticker(hisse.symbol)
        data = stock.history(period='1d')
        if not data.empty:
            latest_price = data['Close'].iloc[-1]
            hisse.price = latest_price
        else:
            hisse.price = None

    return render(request, 'index.html', {'hisse_listesi': hisse_listesi})
