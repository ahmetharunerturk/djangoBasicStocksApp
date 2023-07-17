from django.urls import path
from .views import ana_sayfa

urlpatterns = [
    path('', ana_sayfa, name='ana_sayfa'),
]
