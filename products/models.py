from django.db import models
from categories.models import Category

class Product(models.Model):
  product_id  = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, null=False)
  name        = models.CharField(max_length=50)
  description = models.TextField()
  price       = models.DecimalField(max_digits = 7 , decimal_places = 2)
  quantity    = models.IntegerField()
  avg_rate    = models.FloatField()
  thumbnail   = models.ImageField(default='fallback.png', blank=True)
  category_id = models.ForeignKey(
    Category,
    on_delete=models.CASCADE
  )
