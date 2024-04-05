from django.db import models
from categories.models import Category

class Product(models.Model):
  product_id  = models.AutoField(primary_key=True)
  name        = models.CharField(max_length=50)
  description = models.TextField()
  price       = models.DecimalField(max_digits = 7 , decimal_places = 2)
  quantity    = models.IntegerField()
  avg_rate    = models.FloatField()
  thumbnail   = models.ImageField()
  category_id = models.ForeignKey(
    Category,
    on_delete=models.CASCADE
  )
