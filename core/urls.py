from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from leaflet_map.views import map
from main.views import homepage
from map_api.models import ApartmentSaleHanoi


from ninja import NinjaAPI
from ninja import Schema
from ninja import Router
from typing import List, Optional



from users.api import router as users_router
from map_api.api import router as map_api_router



api = NinjaAPI()
# api = NinjaExtraAPI()
# api.register_controllers(NinjaJWTDefaultController)
router = Router()


api.add_router("/real-estate/", map_api_router)
api.add_router("/users/", users_router)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    # path('predict/', include('map_api.urls')),
    path('', homepage, name='homepage'),
    path('map/', include('leaflet_map.urls')),
    path('api/', api.urls),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('api/users/', include('users.urls'))
]

# https://www.youtube.com/watch?v=6_CL9tyh78w
# add header =  Authentication: Bearer access_token
# POST { "refresh": refresh_token }
# {
#   "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY0NDI0MjQ1NiwiaWF0IjoxNjQ0MTU2MDU2LCJqdGkiOiI2MGJmNDcxNWU4NDU0OTU2ODUyM2MyZGIzMzUxMDk3MiIsInVzZXJfaWQiOiJ2aWV0YW5oMjAwMGFwcmlsQGdtYWlsLmNvbSJ9.21zIQN4mU4UBfCu4eWjnGhzGMZp2cIqfpfGGygJYWnk",
#   "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ0MTU5NjU2LCJpYXQiOjE2NDQxNTYwNTYsImp0aSI6ImMxNjFjMjc1MTllOTQwOWRiZGQ5NzU4NDMzZGM2YjMxIiwidXNlcl9pZCI6InZpZXRhbmgyMDAwYXByaWxAZ21haWwuY29tIn0.FiA9RaoYO6tH5RNZZdw__N5YrzbZLg9cJVYglSobEhU"
# }