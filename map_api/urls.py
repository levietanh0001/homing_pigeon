from django.urls import path, include

from .views import predict_price_apartment


app_name = 'map_api'
urlpatterns = [
    path('', predict_price_apartment, name='predict_price_apartment')
    
]
