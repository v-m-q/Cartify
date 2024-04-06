from rest_framework import serializers
from orderTest.models import Order2
from shoppingCart.serializers import CartItemSerializer

class Order2Serializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True)  

    class Meta:
        model = Order2
        fields = ['order_id', 'user', 'cart_items', 'status', 'created_at']
