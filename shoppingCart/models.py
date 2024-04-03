from django.db import models
from products.models import Product
from user_menna.models import User
from django.core.validators import MinValueValidator



# Create your models here.

class Cart (models.Model):
    cart_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

# Cart model has a ForeignKey relationship with the CartItem model,
# a reverse relation from CartItem to Cart, which is represented by "cartitem_set" is created.
# it returns a Manager that allows you to query all related objects of the CartItem model that are associated with a particular Cart instance
    def total_price(self):
        total = 0
        for item in self.cartitem_set.all():
            total += item.subtotal()
        return total
    
class CartItem (models.Model):
    cartitem_id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('cart', 'product')
def total_price(self):
    return self.product.price * self.quantity

def __str__(self):
    return f"{self.quantity} x {self.product.name}"
    