from multiprocessing import context
from django.shortcuts import render
from django.http import JsonResponse


from .models import ApartmentSaleHanoi








def predict_price_apartment(request):
    if request.method == 'POST':
        address = request.POST['address']
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']
        predicted_price = float(latitude) + float(longitude)
        context = {
            'address': address,
            'latitude': latitude,
            'longitude': longitude,
            'predicted_price': predicted_price
        }
        return JsonResponse({
            'address': address,
            'latitude': latitude,
            'longitude': longitude,
            'predicted_price': predicted_price
        })
        # return render(request, 'prediction/apartment_price.html', context)
    # else:
    #     return render(request, 'prediction/apartment_price.html')