from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator
from django.core.validators import RegexValidator

class LoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['email'] = user.email

        return token

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True,
        validators=[
            RegexValidator(
                
                regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,16}$", 
                message='Password must be between 8 and 16 characters and contain at least one uppercase, one lowercase, one digit, and one special character', 
                code='nomatch')
        ])
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    first_name=serializers.CharField(    
        validators=[
            RegexValidator(
                regex='^[a-zA-Z]{3,}$', 
                message='Name must contain only letters and be at least 3 characters',
                code='nomatch')
        ])
    last_name=serializers.CharField(
        validators=[
            RegexValidator(
                regex='^[a-zA-Z]{3,}$', 
                message='Name must contain only letters and be at least 3 characters long',
                code='nomatch')
        ])
    phone = serializers.CharField(
        validators=[
            RegexValidator(
                regex=r'^01[0-2]{1}[0-9]{8}$',
                message='Phone number must be a valid Egyptian mobile number.',
                code='invalid_phone_number')
        ])
    address = serializers.CharField(
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z0-9\s\-\,\\.\']+$',  
                message='Please enter a valid address.',
                code='invalid_address')
        ])
    class Meta:
        model = User
        fields = ('email','first_name','last_name','password','phone','address')

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone=validated_data['phone'],
            address=validated_data['address']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
    
