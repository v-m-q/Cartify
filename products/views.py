from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status, generics, filters
from rest_framework.decorators import api_view
from .models import Product
from .serializer import ProductSerializer
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 16

@api_view(['GET'])
def getProducts(request):
    try:
        products = Product.objects.all()
        paginator = StandardResultsSetPagination()
        products_for_page = paginator.paginate_queryset(products,request)
        serializer = ProductSerializer(products_for_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    except Exception as e:
        return Response({"message": "An error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def GetProduct(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getProductsByCategory(request, category_id):
    try:
        products = Product.objects.filter(id=category_id)
        paginator = StandardResultsSetPagination()
        productd_for_page = paginator.paginate_queryset(products,request)
        serializer = ProductSerializer(productd_for_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description', 'category_id__name']
    pagination_class = StandardResultsSetPagination
