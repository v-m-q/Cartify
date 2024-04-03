from django.db import IntegrityError
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


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addItem(request):
    product_id = request.data.get('product_id')
    quantity = int(request.data.get('quantity', 1))
    
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return Response({"error": "Product does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    try:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, cart_item_created = CartItem.objects.get_or_create(cart=cart, product=product)
        
        if not cart_item_created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
        
        cart_item.save()
        
        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    except IntegrityError:
        return Response({"error": " Process faild. Please try again later."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def removeItem(request, cart_item_id):
    try:
        cart_item = CartItem.objects.get(pk=cart_item_id)
    except CartItem.DoesNotExist:
        return Response({"error": "Cart item does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    cart_item.delete()
    return Response({" Deleted Successfully "},status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateQuantity(request, cart_item_id):
    try:
        cart_item = CartItem.objects.get(pk=cart_item_id)
    except CartItem.DoesNotExist:
        return Response({"error": "Cart item does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    new_quantity = int(request.data.get('quantity', cart_item.quantity))
    cart_item.quantity = new_quantity
    cart_item.save()
    
    serializer = CartItemSerializer(cart_item)
    return Response(serializer.data, status=status.HTTP_200_OK)






