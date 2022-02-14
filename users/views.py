#==================================#
#=== Session-based Authentication ===#
#==================================#


from django.contrib.auth import authenticate
from django.shortcuts import redirect, render
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse # convert named url to relative url
from django.contrib import messages # log to admin login page


from .models import CustomUser


from .forms import CustomUserLoginForm


# app_name = 'users'
def login_user(request):
    django_logout(request)
    message = ''
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            django_login(request, user)
            return redirect('homepage')
        else:
            message = "Log in failed!"
            # messages.error(request, message)
            context = {
                'message': message
            }
            return render(request, 'users/login.html', context)
            # return redirect('users:login_user')
    else:
        # message = f"Login: Something wrong with request: {request.method}"
        # messages.error(request, message)
        return render(request, 'users/login.html')



@login_required(login_url='users/login/')
def logout_user(request):
    django_logout(request)
    return redirect('homepage')
    
    
def register_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if confirm_password == password:
            # user = CustomUser(email=email, password=password)
            user = CustomUser()
            user.email = email
            user.set_password(password)
            user.save()
            return redirect('users:login_user')
        else:
            # message = "Confirm password must match password!"
            # messages.error(request, message)
            return redirect('users:register_user')
    else:
        # message = f"Register: Something wrong with request: {request.method}"
        # messages.error(request, message)
        return render(request, 'users/register.html')
    
    # custom session-based user permissions
    # https://stackoverflow.com/questions/65501503/make-that-django-simple-jwt-have-the-same-permissions-as-django-admin
#==================================#
#=== Token-based Authentication ===#
#==================================#

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.exceptions import AuthenticationFailed
# from .serializers import UserSerializer
# from .models import CustomUser
# import jwt, datetime
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework.permissions import AllowAny
# from rest_framework import permissions, status, generics
# from rest_framework.generics import GenericAPIView


# from .serializers import LogoutSerializer




# class UserList(APIView):
#     def get(self, request):
#         email = request.data['email']
#         user = CustomUser.objects.filter(email=email).first()
#         serializer = UserSerializer(user)
#         return Response(serializer.data)
    

    
# class RegisterView(APIView):
#     permission_classes = [AllowAny]
#     def post(self, request, format='json'):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             if user:
#                 json = serializer.data
#                 return Response(json, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class LoginView(APIView):
#     def post(self, request):
#         email = request.data['email']
#         password = request.data['password']

#         user = CustomUser.objects.filter(email=email).first()

#         if user is None:
#             raise AuthenticationFailed('User not found!')

#         if not user.check_password(password):
#             raise AuthenticationFailed('Incorrect password!')

#         payload = {
#             # 'id': user.id,
#             'email': user.email,
#             'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
#             'iat': datetime.datetime.utcnow()
#         }

#         token = jwt.encode(payload, 'secret', algorithm='HS256')

#         response = Response({'message': 'success'})

#         response.set_cookie(key='jwt', value=token, httponly=True)
        
        
#         response.data = {
#             'jwt': token
#         }
#         return response



# class UserView(APIView):
#     def get(self, request):
#         token = request.COOKIES.get('jwt')

#         if not token:
#             raise AuthenticationFailed('Unauthenticated!')

#         try:
#             payload = jwt.decode(token, 'secret', algorithms=['HS256'])
#         except jwt.ExpiredSignatureError:
#             raise AuthenticationFailed('Unauthenticated!')

#         user = CustomUser.objects.filter(email=payload['email']).first()
#         serializer = UserSerializer(user)
#         return Response(serializer.data)


    
# class LogoutView(generics.GenericAPIView):
#     serializer_class = LogoutSerializer
#     permission_classes = (permissions.IsAuthenticated,)
    
    
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(status=status.HTTP_204_NO_CONTENT)    
