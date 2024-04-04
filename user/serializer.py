from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['user']
    


    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True)
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    first_name=serializers.CharField()
    last_name=serializers.CharField()

    class Meta:
        model = User
        fields = ('email','first_name','last_name','password')

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
    

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['email'] = user.email

        return token
