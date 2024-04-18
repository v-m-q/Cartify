from django.db import models
from categories.models import Category
from django.db.models import Avg

class Product(models.Model):
  name        = models.CharField(max_length=50)
  description = models.TextField()
  price       = models.DecimalField(max_digits = 7 , decimal_places = 2)
  quantity    = models.IntegerField()
  thumbnail   = models.ImageField(default='fallback.png', blank=True)
  avg_rate    = models.DecimalField(max_digits=3, decimal_places=1, blank=True, default=0)
  category    = models.ForeignKey(Category, on_delete=models.CASCADE)

  def calculate_avg_rating(self):
    avg_rating = self.rating_set.aggregate(avg_rating=Avg('value'))['avg_rating']
    return avg_rating if avg_rating else 0.0

  @property
  def avg_rating(self):
    return self.calculate_avg_rating() or 0

  def __str__(self):
    return self.name