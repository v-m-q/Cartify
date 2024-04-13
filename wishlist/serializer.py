# from rest_framework import serializers
# from .models import Wishlist
# from products.serializer import ProductSerializer
# from user.serializer import RegisterSerializer

# class WishlistSerializer(serializers.ModelSerializer):
#     product_details = serializers.SerializerMethodField()

#     class Meta:
#         model = Wishlist
#         fields = '__all__' #['id', 'user_id', 'product', 'product_details']

#     def get_product_details(self, obj):
#         product = obj.product
#         serializer = ProductSerializer(many=False)
#         return serializer.data

# class WishlistSerializer(serializers.ModelSerializer):
#     product = ProductSerializer(many=False) 
#     user = RegisterSerializer(many=False)
#     class Meta:
#         model = Wishlist
#         fields = '__all__'

# class CartSerializer(serializers.ModelSerializer):
#     cartitem_set = CartItemSerializer(many=True, read_only=True)

#     class Meta:
#         model = Cart
#         fields = '__all__'

# from rest_framework import serializers
# from .models import Wishlist
# from products.serializer import ProductSerializer

# class WishlistSerializer(serializers.ModelSerializer):
#     product_details = serializers.SerializerMethodField()

#     class Meta:
#         model = Wishlist
#         fields = ['id', 'user', 'product', 'product_details']
#         read_only_fields = ['user'] 

#     def get_product_details(self, obj):
#         product = obj.product
#         serializer = ProductSerializer(product, many=False)
#         return serializer.data

# serializers.py
from rest_framework import serializers
from .models import Wishlist

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'
