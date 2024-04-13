from rest_framework import serializers
from categories.serializer import CategorySerializer
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    # category_name = serializers.SerializerMethodField()

    class Meta:
        model=Product
        fields='__all__' #, 'name', 'description', 'price', 'quantity', 'avg_rate', 'thumbnail', 'category_id' , 'category_name']
        # fields=['product_id', 'name', 'description', 'price', 'quantity', 'avg_rate', 'thumbnail', 'category_id' , 'category_name']

    def to_representation(self, instance):
        rep = super(ProductSerializer, self).to_representation(instance)
        rep['category'] = instance.category.name
        return rep


    # def get_category_name(self, obj):
    #     category = obj.category_id
    #     serializer = CategorySerializer(category)
    #     return serializer.data