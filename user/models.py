from enum import Enum
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
# Create your models here.
class User(AbstractUser):

    GENDER_CHOICES = [
        ("F", 'Female'),
        ("M", 'Male'),
    ]
    first_name = models.CharField(
        max_length=50,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z]{3,}$', 
                message='Name must contain only letters and be at least 3 characters long',
                code='nomatch')
        ])
    last_name = models.CharField(
        max_length=50,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z]{3,}$', 
                message='Name must contain only letters and be at least 3 characters long',
                code='nomatch')
        ])
    email = models.EmailField(max_length=255,unique=True)
    password=models.CharField(
        max_length=16,
        validators=[
            RegexValidator(
                
                regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,16}$", 
                message='', 
                code='nomatch')
        ])
    gender=models.CharField(max_length=6,choices=GENDER_CHOICES)
