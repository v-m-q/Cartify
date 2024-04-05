from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email,password,first_name,last_name,phone=None,address=None):
        if not email:
            raise ValueError('The Email field must be set')
        if not first_name:
            raise ValueError('The First name field must be set')
        if not last_name:
            raise ValueError('The First name field must be set')
        
        email = self.normalize_email(email)
        user = self.model(email=email,first_name=first_name,last_name=last_name)
        user.phone = phone
        user.address = address
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password,**extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        super_user = self.create_user(email=email, password=password, first_name=first_name, last_name=last_name)
        super_user.is_staff = True
        super_user.is_superuser = True
        # super_user.gender = "M"
        super_user.save()
        return super_user



class User(AbstractBaseUser):

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
        max_length=255,
        validators=[
            RegexValidator(
                
                regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,16}$", 
                message='', 
                code='nomatch')
        ])
    phone = models.CharField(max_length=11, null=True,blank=True)
    address = models.CharField(max_length=255, null=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser =  models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["first_name","last_name"]

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    def __str__(self):
        return self.email
