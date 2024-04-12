from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status, generics, filters
from rest_framework.decorators import api_view
from products.models import Product
from products.serializer import ProductSerializer

@api_view(['GET'])
def getHomeData(request):
    try:
        highest_rated_products = Product.objects.order_by('-avg_rate')[:3]
        latest_products = Product.objects.order_by('-id')[:8]
        
        highest_serializer = ProductSerializer(highest_rated_products, many=True)
        latest_serializer = ProductSerializer(latest_products, many=True)
        
        result = {
            'highest_rated_products': highest_serializer.data,
            'latest_products': latest_serializer.data
        }
        
        return Response(result, status=status.HTTP_200_OK)
    
    except Exception as e:
        error_message = str(e)
        return Response({'error': error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)