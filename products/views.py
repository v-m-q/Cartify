from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status, generics, filters
from rest_framework.decorators import api_view
from .models import Product
from .serializer import ProductSerializer

# /products 
@api_view(['GET'])
def getProducts(request):
    try:
        products = Product.objects.all()
        if not products:
            return JsonResponse({"message": "Somethinh Go Wrong"}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return JsonResponse({"message": "An error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def GetProduct(request, ProductId):
    try:
        product = Product.objects.get(id=ProductId)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description', 'category_id__name']
    ordering_fields = ['name']
