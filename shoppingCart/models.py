from django.db import models
from products.models import Product
from user.models import User
from django.core.validators import MinValueValidator

# Create your models here.
class Cart (models.Model):
    cart_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def total_price(self):
        total = 0
        for item in self.cartitem_set.all():
            total += item.total_item_price()
        return total
    
class CartItem(models.Model):
    STATUS_CHOICES = [
        ('onCart', 'OnCart'),
        ('done', 'Done')
    ]
    cartitem_id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='onCart')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('cart', 'product')
        
    def total_item_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
