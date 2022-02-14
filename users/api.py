from ninja import NinjaAPI
from ninja import Schema
from ninja import Router
from typing import List, Optional


from .models import CustomUser


router = Router()

@router.get("/all")
def list_users(request):
    return [
        {
            "id": u.id,
            "email": u.email,
            "password": u.password
        }
        for u in CustomUser.objects.all()
    ]
    
    
@router.get("/filter/id={user_id}")
def user_details(request, user_id: int):
    u = CustomUser.objects.get(id=user_id)
    return {
        "id": u.id,
        "email": u.email,
        "password": u.password
    }