from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from .models import Order, OrderItem
from products.models import Product
from user.models import User
from .serializers import OrderItemsSerializer, OrderSerializer
from rest_framework.pagination import PageNumberPagination
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 12

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_orders(request):
    orders = Order.objects.filter(user_id=request.user)  
    paginator = StandardResultsSetPagination()
    orders_for_page = paginator.paginate_queryset(orders,request)
    serializer = OrderSerializer(orders_for_page, many=True)
    return paginator.get_paginated_response(serializer.data)
@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_status(request, order_id):
    try:
        order = Order.objects.get(order_id=order_id)
    except Order.DoesNotExist:
        return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
    if order.user != request.user:
        return Response({'error': 'You are not authorized to update this order'}, status=status.HTTP_403_FORBIDDEN)
    
    serializer = OrderSerializer(order, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_order_items(request,order_id):
    order_id = order_id
    if not order_id:
        return Response({'error': 'Order ID is required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
    if order.user != request.user:
        return Response({'error': 'You are not authorized to view this order'}, status=status.HTTP_403_FORBIDDEN)
    items = OrderItem.objects.filter(order_id = order_id)

    serializer = OrderItemsSerializer(items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_order_item(request, order_id, item_id):
    order_item_id = item_id
    if not order_item_id:
        return Response({'error': 'Order Item ID is required'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        order_item = OrderItem.objects.get(order_item_id=order_item_id)
    except OrderItem.DoesNotExist:
        return Response({'error': 'Order Item not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if order_item.order.user != request.user:
        return Response({'error': 'You are not authorized to view this order item'}, status=status.HTTP_403_FORBIDDEN)
    
    serializer = OrderItemsSerializer(order_item)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_order(request):
        request.data['user'] = request.user.id
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_item(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
    
    try:
        product_id = request.data['product']
        quantity = int(request.data['quantity'])
    except KeyError:
        return Response({'error': 'Product ID and quantity are required'}, status=status.HTTP_400_BAD_REQUEST)
    except ValueError:
        return Response({'error': 'Invalid quantity'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    if quantity <= 0:
        return Response({'error': 'Invalid quantity'}, status=status.HTTP_400_BAD_REQUEST)

    if quantity > product.quantity:
        return Response({'error': 'This product is un available'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = OrderItemsSerializer(data=request.data, context={'order': order, 'product': product})
    if serializer.is_valid():
        product.quantity -= quantity
        product.save()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_order(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
    if order.user != request.user:
        return Response({'error': 'You are not authorized to delete this order'}, status=status.HTTP_403_FORBIDDEN)
    
    order.delete()
    return Response({'message': 'Deleted Successfully'},status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_item(request, order_id, item_id):
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
    try:
        order_item = OrderItem.objects.get(order=order, id=item_id)
    except OrderItem.DoesNotExist:
        return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
    if order_item.order.user != request.user:
        return Response({'error': 'You are not authorized to delete this item'}, status=status.HTTP_403_FORBIDDEN)
    order_item.delete()
    return Response({'message': 'Deleted Successfully'},status=status.HTTP_204_NO_CONTENT)
    