from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import LoginSerializer, RegisterSerializer
from .models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.decorators import (api_view,permission_classes)

# Create your views here.

#Login User
class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

#Register User
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
