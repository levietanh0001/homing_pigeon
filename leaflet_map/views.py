from django.shortcuts import render

from map_api.models import ApartmentSaleHanoi



def map(request):
    addresses = list(ApartmentSaleHanoi.objects.values_list("address", flat=True))
    context = {
        'addresses': addresses
    }
    return render(request, 'leaflet_map/real_estate.html', context)