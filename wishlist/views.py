from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Wishlist
from .serializer import WishlistSerializer

@api_view(['GET'])
@login_required
def getProductsByWishlist(request):
    try:
        wishlist_items = Wishlist.objects.filter(user=request.user)
        serializer = WishlistSerializer(wishlist_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Wishlist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@login_required
def addProductsToWishlist(request):
    if request.method == 'POST':
        serializer = WishlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

def removeProductsToWishlist(request):
    pass