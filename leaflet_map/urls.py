from django.urls import path, include
from django.shortcuts import render



from .views import map


app_name = 'leaflet_map'
urlpatterns = [
    path('real-estate/', map, name='real-estate'),
]
