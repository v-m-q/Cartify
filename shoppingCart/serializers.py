from rest_framework import serializers
from .models import  Cart, CartItem
from products.serializer import ProductSerializer
from user_menna.serializers import UserSerializer

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False) 

    class Meta:
        model = CartItem
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    cartitem_set = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = '__all__'