from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User 
        fields = ['first_name', 'last_name',  'email', 'phone'] 
 
    # def update(self, instance, validated_data):
    #     instance.first_name = validated_data.get('first_name', instance.first_name)
    #     instance.save()
    #     return instance       
    # def update(self, instance, validated_data):
    #     instance.first_name = validated_data['first_name']
        # instance.last_name = validated_data['last_name']
        # instance.username = validated_data['phone']
        # instance.email = validated_data['email']
        # instance.save()
        # return instance