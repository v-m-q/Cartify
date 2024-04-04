from rest_framework import serializers
from .models import Wishlist
from products.serializer import ProductSerializer

class WishlistSerializer(serializers.ModelSerializer):
    product_details = serializers.SerializerMethodField()

    class Meta:
        model = Wishlist
        fields = ['id', 'user', 'product', 'product_details']

    def get_product_details(self, obj):
        product = obj.product
        serializer = ProductSerializer(product)
        return serializer.data
