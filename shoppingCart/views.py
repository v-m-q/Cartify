from django.shortcuts import render
from user_menna.models import User
from products.models import Product
from .models import Cart , CartItem 
from rest_framework import status
from .serializers import CartItemSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# # Create your views here.

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Cart
from .serializers import CartSerializer


#### get cart
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getCart(request):
    try:
        cart = Cart.objects.filter(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data , status=status.HTTP_200_OK)
    except Cart.DoesNotExist:
        return Response({'detail': 'Cart not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# def add_to_cart(request,):
#     product = get_object_or_404(Product,id=pk)
#     cart = Cart.objects.get(user=request.user)
#     cart_item = CartItem.objects.create(user=request.user,product=product,quantity=1,price=product.price,total_price=product.price)
#     cart.items.add(cart_item)
#     serializer = CartItemSerializer(cart_item,many=False)
#     return Response(serializer.data)


# @api_view(['PUT'])
# @permission_classes([IsAuthenticated])

# def update_cart(request,pk):
#     product = get_object_or_404(Product,id=pk)
#     cart = Cart.objects.get(user=request.user)
#     cart_item = CartItem.objects.get(user=request.user,product=product)
#     cart_item.quantity = request.data['quantity']
#     cart_item.total_price = request.data['quantity'] * product.price
#     cart_item.save()
#     serializer = CartItemSerializer(cart_item,many=False)
#     return Response(serializer.data)

# @api_view(['DELETE'])
# @permission_classes([IsAuthenticated])

# def delete_cart(request,pk):
#     product = get_object_or_404(Product,id=pk)
#     cart = Cart.objects.get(user=request.user)
#     cart_item = CartItem.objects.get(user=request.user,product=product)
#     cart.items.remove(cart_item)
#     serializer = CartItemSerializer(cart_item,many=False)
#     return Response(serializer.data)

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])

# def get_cart(request):
#     cart = Cart.objects.get(user=request.user)
#     serializer = CartItemSerializer(cart.items.all(),many=True)
#     return Response(serializer.data)

# @api_view(['PUT'])
# @permission_classes([IsAuthenticated])

# def increse_quantity(request,pk):
#     product = get_object_or_404(Product,id=pk)
#     cart = Cart.objects.get(user=request.user)
#     cart_item = CartItem.objects.get(user=request.user,product=product)
#     cart_item.quantity += 1
#     cart_item.total_price = cart_item.quantity * product.price
#     cart_item.save()
#     serializer = CartItemSerializer(cart_item,many=False)
#     return Response(serializer.data)

# @api_view(['PUT'])
# @permission_classes([IsAuthenticated])

# def decrese_quantity(request,pk):
#     product = get_object_or_404(Product,id=pk)
#     cart = Cart.objects.get(user=request.user)
#     cart_item = CartItem.objects.get(user=request.user,product=product)
#     cart_item.quantity -= 1
#     cart_item.total_price = cart_item.quantity * product.price
#     cart_item.save()
#     serializer = CartItemSerializer(cart_item,many=False)
#     return Response(serializer.data)

# # @api_view(['GET'])
# # @permission_classes([IsAuthenticated])

# # def get_total_price(request):
# #     cart = Cart.objects.get(user=request.user)
# #     serializer = CartItemSerializer(cart.items.all(),many=True)
# #     return Response(serializer.data)


#     # >>> add url
#     # urlpatterns = [
#     #     path('add-to-cart/<int:pk>', add_to_cart, name='add-to-cart'),
#     #     path('update-cart/<int:pk>', update_cart, name='update-cart'),
#     #     path('delete-cart/<int:pk>', delete_cart, name='delete-cart'),
#     #     path('get-cart', get_cart, name='get-cart'),
#     #     path('increse-quantity/<int:pk>', increse_quantity, name='increse-quantity'),
#     #     path('decrese-quantity/<int:pk>', decrese_quantity, name='decrese-quantity'),
#     #     path('get-total-price', get_total_price, name='get-total-price'),
#     # ]


# # >>> error handleing

# # def error_handler(exc, context):
# #     # Call REST framework's default error handler first,
# #     # to get the standard error response.
# #     response = super().error_handler(exc, context)


# # >>> add status and respons messages

#     # def get_response(self, request):
#     #     response = super().get_response(request)
#     #     response.status_code = status.HTTP_400_BAD_REQUEST
#     #     return response

#     # def process_exception(self, exc):
#     #     response = super().process_exception(exc)
#     #     response.status_code = status.HTTP_400_BAD_REQUEST
#     #     return response

#     # def handle_no_permission(self, request):
#     #     response = super().handle_no_permission(request)
#     #     response.status_code = status.HTTP_403_FORBIDDEN
#     #     return response

#     # def handle_exception(self, exc):
#     #     response = super().handle_exception(exc)
#     #     response.status_code = status.HTTP_400_BAD_REQUEST
#     #     return response

#     # def handle_error(self, exc):
#     #     response = super().handle_error(exc)
#     #     response.status_code = status.HTTP_400_BAD_REQUEST
#     #     return response

#     # def handle_not_found(self, exc):
#     #     response = super().handle_not_found(exc)
#     #     response.status_code = status.HTTP_404_NOT_FOUND
#     #     return response

#     # def handle_bad_request(self, exc):
#     #     response = super().handle_bad_request(exc)
#     #     response.status_code = status.HTTP_400_BAD_REQUEST
#     #     return response

#     # def handle_method_not_allowed(self, exc):
#     #     response = super().handle_method_not_allowed(exc)
#     #     response.status_code = status.HTTP_405_METHOD_NOT_ALLOWED
#     #     return response

#     # def handle_not_acceptable(self, exc):
#     #     response = super().handle_not_acceptable(exc)
#     #     response.status_code = status.HTTP_406_NOT_ACCEPTABLE
#     #     return response

#     # def handle_internal_server_error(self, exc):
#     #     response = super().handle_internal_server_error(exc)
#     #     response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
#     #     return response

#     # def handle_not_implemented(self, exc):
#     #     response = super().handle_not_implemented(exc)
#     #     response.status_code = status.HTTP_501_NOT_IMPLEMENTED
#     #     return response

#     # def handle_bad_gateway(self, exc):
#     #     response = super().handle_bad_gateway(exc)
#     #     response.status_code = status.HTTP_502_BAD_GATEWAY
#     #     return response

#     # def handle_service_unavailable(self, exc):
#     #     response = super().handle_service_unavailable(exc)
#     #     response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
#     #     return response