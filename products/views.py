from urllib import response
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Product
from .serializer import ProductSerializer

# Create your views here.

# /products 
@api_view(['GET'])
def getProducts(request):
    try:
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"message": "An error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def GetProduct(request,ProductId):
    try:
        product = Product.objects.get(id=ProductId)
        serializer = ProductSerializer(product)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
