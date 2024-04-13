from django.db import IntegrityError
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from products.models import Product
from .models import Cart, CartItem 
from .serializers import CartItemSerializer , CartSerializer
from user.models import User
from orders.models import Order , OrderItem
from orders.serializers import OrderItemsSerializer , OrderSerializer

# Create your views here.
def get_cart_item(user):
    try:
        cart = Cart.objects.get(user_id=user)
        cart_items = cart.cartitem_set.filter(status='onCart') 
        serializer = CartItemSerializer(cart_items, many=True)
        return serializer.data
    except Cart.DoesNotExist:
        return []
    except Exception as e:
        return []

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_cart(request):
    try:
        cart = Cart.objects.get(user_id=request.user)
        cart_items = cart.cartitem_set.filter(status='onCart') 
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Cart.DoesNotExist:
        return Response({'detail': 'Cart not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_item(request):
    product_id = request.data.get('product_id')
    quantity = int(request.data.get('quantity', 1))
    
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return Response({"error": "Product does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    try:
        if (product.quantity == 0):
            return Response({"error": "product is unavailable"}, status=status.HTTP_400_BAD_REQUEST)
        elif (quantity > product.quantity) :
            return Response({"error": "Quantity is more than available"}, status=status.HTTP_400_BAD_REQUEST)
        cart, created = Cart.objects.get_or_create(user_id=request.user.id)
        cart_item, cart_item_created = CartItem.objects.get_or_create(cart=cart, product=product)
            
        if not cart_item_created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
            
        product.quantity = product.quantity - quantity
        product.save()
        # product.quantity = product.quantity - quantity
        # product.save()
        cart_item.save()
            
        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except IntegrityError:
        return Response({"error": " Process faild. Please try again later."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_item(request, cart_item_id):
    try:
        cart_item = CartItem.objects.get(pk=cart_item_id)
    except CartItem.DoesNotExist:
        return Response({"error": "Cart item does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    cart_item.product.quantity += cart_item.quantity
    cart_item.product.save()
    # cart_item.product.quantity += cart_item.quantity
    # cart_item.product.save()
    cart_item.delete()
    return Response({"Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)



@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_quantity(request, cart_item_id):
    try:
        cart_item = CartItem.objects.get(pk=cart_item_id)
    except CartItem.DoesNotExist:
        return Response({"error": "Cart item does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    new_quantity = int(request.data.get('quantity', cart_item.quantity))
    
    if (new_quantity > cart_item.product.quantity) :
        return Response({"error": "Quantity is more than available"}, status=status.HTTP_404_NOT_FOUND)
    elif (new_quantity == 0 or new_quantity < 0):
        return Response({"error": "Invalid quantity"}, status=status.HTTP_404_NOT_FOUND)
    cart_item.quantity = new_quantity
    cart_item.save()
    
    serializer = CartItemSerializer(cart_item)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_total_price(request):
    try:
        cart = Cart.objects.get(user_id=request.user)
        total_price = cart.total_price()
        return Response({"total_price": total_price }, status=status.HTTP_200_OK)
    except Cart.DoesNotExist:
        return Response({"error": "Cart does not exist"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def change_cart_item_status(request, cart_item_id):
    try:
        cart_item = CartItem.objects.get(pk=cart_item_id)
        if cart_item.cart.user == request.user:
            new_status = request.data.get('status', None)
            if not new_status:
                return Response({'detail': 'New status is required.'}, status=status.HTTP_400_BAD_REQUEST)
    
            if new_status not in ['onCart', 'done']:
                return Response({'detail': 'Status should be either "onCart" or "done".'}, status=status.HTTP_400_BAD_REQUEST)

            cart_item.status = new_status
            cart_item.save()

            serializer = CartItemSerializer(cart_item)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'You are not allowed to change this item.'}, status=status.HTTP_403_FORBIDDEN)
    except CartItem.DoesNotExist:
        return Response({'detail': 'Cart item not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def checkout(request):
    try:
        user = request.user
        user_cart = get_object_or_404(Cart, user_id=user)
    except Cart.DoesNotExist:
        return Response({'detail': 'Cart not found'}, status=status.HTTP_404_NOT_FOUND)

    items = get_cart_item(user)
    user_instance = User.objects.get(email=user.email)
    total_price = request.data.get('total_price')  
    print(total_price)
    order_serializer = OrderSerializer(data={'user': user_instance.pk,'total_price':total_price, 'status': 'pending'})

    if order_serializer.is_valid():
        order = order_serializer.save()  

        for item in items:
            order_item_data = {
                'order': order.pk,  
                'product': item['product']['id'],  
                'quantity': item['quantity']  
            }
            order_item_serializer = OrderItemsSerializer(data=order_item_data)
            if order_item_serializer.is_valid():
                order_item_serializer.save()  
                product_order = Product.objects.get(id = item['product']['id'])
                print(product_order)
                product_order.quantity = product_order.quantity - item['quantity']
                product_order.save()
                item['status'] = 'done'
            else:
                return Response(order_item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user_cart.cartitem_set.all().delete()

        return Response(order_serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
