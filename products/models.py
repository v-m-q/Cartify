from django.db import models
from categories.models import Category

class Product(models.Model):
  name        = models.CharField(max_length=50)
  description = models.TextField()
  price       = models.FloatField()
  quantity    = models.IntegerField()
  avg_rate    = models.FloatField()
  thumbnail   = models.ImageField()
  category_id = models.ForeignKey(
    Category,
    on_delete=models.CASCADE
  )

  def __str__(self):
    return self.name
