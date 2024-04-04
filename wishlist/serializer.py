from rest_framework import serializers
from .models import Wishlist
from products.serializer import ProductSerializer

class WishlistSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Wishlist
        fields = '__all__'