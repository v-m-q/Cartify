from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from products.models import Product
from .models import Wishlist
from django.http import JsonResponse
from .serializer import WishlistSerializer
from rest_framework.pagination import PageNumberPagination
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 16

@api_view(['GET'])
def getProductsByWishlist(request):
    try:
        wishlist_items = Wishlist.objects.filter(user_id=request.user)
        paginator = StandardResultsSetPagination()
        wishlist_items_for_page = paginator.paginate_queryset(wishlist_items,request)
        serializer = WishlistSerializer(wishlist_items_for_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    except Wishlist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addProductsToWishlist(request):
    # Assuming the request data contains 'product_id'
    product_id = request.data.get('product')

    if not product_id:
        return Response({'error': 'Product ID is required'}, status=400)

    # Assuming the user is available through request.user
    user = request.user

    # Check if the product is already in the wishlist
    if Wishlist.objects.filter(user=user, product_id=product_id).exists():
        return Response({'error': 'Product already in wishlist'}, status=400)

    # Create a new Wishlist item
    wishlist_item = Wishlist.objects.create(user=user, product_id=product_id)

    # Serialize the created item
    serializer = WishlistSerializer(wishlist_item)

    return Response(serializer.data, status=201)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def removeProductsToWishlist(request):
    try:
        product_id = request.data.get('product')
        wishlist_item = Wishlist.objects.filter(user_id=request.user, product_id=product_id)
        if wishlist_item:
            wishlist_item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"error": "Wishlist item does not exist."})
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
