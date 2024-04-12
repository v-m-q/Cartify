from rest_framework import serializers
from categories.serializer import CategorySerializer
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    # category_name = serializers.SerializerMethodField()

    class Meta:
        model=Product
        fields='__all__'
        # fields=['id', 'name', 'description', 'price', 'quantity', 'avg_rate', 'thumbnail', 'category_id' , 'category_name']
        

    def get_category_name(self, obj):
        category = obj.category_id
        serializer = CategorySerializer(category)
        return serializer.data