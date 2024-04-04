from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from .models import User
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

# def home(request):
#     return render(request , 'home.html')
@api_view(['GET'])
def get_book(request):
    book_objs = User.objects.all()
    serializer = UserSerializer(book_objs , many=True)
    return Response({'status' : 200 , 'payload' : serializer.data})
    

from rest_framework_simplejwt.tokens import RefreshToken
    
class RegisterUser(APIView):
    def post(self , request):
        serializer = UserSerializer(data = request.data)

        if not serializer.is_valid():
            return Response({'status' : 403 ,'errors' : serializer.errors , 'messge' : 'Something went wrong'})
            
        serializer.save()  

        user = User.objects.get(username = serializer.data['username'])
        refresh = RefreshToken.for_user(user)
        
        
        return Response({'status' : 200 ,
        'payload' : serializer.data,
        'refresh': str(refresh),
        'access': str(refresh.access_token), 'messge' : 'your data is saved'})

        

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404

class StudentAPI(APIView):
    authentication_classes = [ JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print(request)
        userData = User.objects.filter(email=request.user)
        serializer = UserSerializer(userData, many=True)
        return Response({'status' : 200 , 'payload' : serializer.data})
    
    def put(self, request):
        print(request.user)
        user_instance = get_object_or_404(User, email=request.user) #User.objects.filter(email=request.user).first()            
        serializer = UserSerializer(user_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'message': 'User updated successfully', 'payload': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
       
        
            

    
