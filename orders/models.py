from django.db import models
from user.models import User

# Create your models here.

class Order(models.Model):
    OrderStatus_Choices=[
     ( "pending" ,'Pending'),
     ( "shipped" ,'Shipped'),
     ( "delivered" ,'Delivered')
    ]

    total_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=50,choices=OrderStatus_Choices,default="pending")
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)    
