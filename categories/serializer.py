from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
        # fields=['id', 'name', 'description', 'price', 'quantity', 'avg_rate', 'thumbnail', 'category_id' ]
