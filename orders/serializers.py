from rest_framework import serializers
from user.models import User
from user.serializer import RegisterSerializer

from products.serializer import ProductSerializer
from .models import Order, OrderItem


class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"



class OrderSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())  
    orderitems = OrderItemsSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
