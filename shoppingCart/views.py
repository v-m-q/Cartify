from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from user_menna.models import User
from products.models import Product
from .models import Cart , CartItem 
from .serializers import CartItemSerializer , CartSerializer

# Create your views here.


#### get cart
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getCart(request):
    try:
        cart = Cart.objects.filter(user=request.user)
        if cart.exists(): 
            serializer = CartSerializer(cart, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Cart not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


