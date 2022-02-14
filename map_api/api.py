from ninja import NinjaAPI
from ninja import Schema
from ninja import Router
from typing import List, Optional
from django.forms.models import model_to_dict
from django.http import JsonResponse
import json


from .models import ApartmentSaleHanoi



api = NinjaAPI()
router = Router()


class ApartmentSaleHanoiSchema(Schema):
    title: str
    address: str
    latitude: float
    longitude: float
    price_by_area: int
class PredictApartmentSaleHanoiSchema(Schema):
    price_by_area: float
class Apartment(Schema):
    address: str = None
    latitude: str
    longitude: str
    direction: str = None
    paper: str = None
    

@router.get('/apartment-sale-hanoi/', response=ApartmentSaleHanoiSchema)
def apartment_sale_hanoi(request, limit: Optional[str] = None, address: Optional[str] = None):
    response = ApartmentSaleHanoi.objects.all()
    if address:
        ash_by_address = ApartmentSaleHanoi.objects.get(address=address)
        # response = model_to_dict(ash_by_address)
        response = ash_by_address
    if limit:
        response = ApartmentSaleHanoi.objects.all()[:int(limit)]
    return response

test_arr = ['hello', 'world']
# @router.get('/apartment-sale-hanoi-price/predict', latitude: float, longitude:float, response=ApartmentSaleHanoiPredictSchema)
# def apartment_sale_hanoi_predict(request, latitude: Optional[str] = None, longitude: Optional[str] = None):
@router.get('/apartment-sale-hanoi-price/predict')
def apartment_sale_hanoi_predict(request, apartment: Apartment):

    predicted_price = float(apartment.latitude) + float(apartment.longitude)
    data = {
        'predicted_price': predicted_price   
    }
    response = json.dumps(data)
    return response

weapons = ["Ninjato", "Shuriken", "Katana", "Kama", "Kunai", "Naginata", "Yari"]
@router.get("/weapons")
def list_weapons(request, limit: int = 2, offset: int = 0):
    return weapons[offset: offset + limit]

class Item(Schema):
    name: str
    description: str = None
    price: float
    quantity: int


@router.get("/items")
def get_items(request, item: Item):
    return item