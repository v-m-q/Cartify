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

class StudentAPI(APIView):
    authentication_classes = [ JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # student_objs = Student.objects.all()
        print(request)
        userData = User.objects.filter(email=request.user)
        serializer = UserSerializer(userData, many=True)
        return Response({'status' : 200 , 'payload' : serializer.data})
    
        # serializer = UserSerializer(User.objects.filter , many=True)
        # return Response(serializer.data, status=status.HTTP_200_OK)
       
    def post(self, request):
        serializer = UserSerializer(data = request.data)

        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status' : 403 ,'errors' : serializer.errors , 'messge' : 'Something went wrong'})
            
        serializer.save()   
        return Response({'status' : 200 , 'payload' : serializer.data , 'messge' : 'your data is saved'})

   
    def put(self, request):
        pass
    
    def patch(self,request):
        try:
            student_obj = User.objects.get(id = request.data['id'])
            serializer = UserSerializer(student_obj , data = request.data , partial =True)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status' : 403 ,'errors' : serializer.errors , 'messge' : 'Something went wrong'})
                
            serializer.save()   
            return Response({'status' : 200 , 'payload' : serializer.data , 'messge' : 'your data is updated'})

        except Exception as e:
            print(e)
            return Response({'status' :403 , 'message' : 'invalid id'})
   
    def delete(self, request):
        try:
            id = request.GET.get('id')
            student_obj = User.objects.get(id = id)    
            student_obj.delete()
            return Response({'status' : 200, 'message' : 'deleted'})
    
        except Exception as e:
            print(e)
            return Response({'status' :403 , 'message' : 'invalid id'})
        
            

    
