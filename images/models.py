from django.db import models
from products.models import Product

class Images(models.Model):
  # id    = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, null=False)
  image   = models.CharField(max_length=50)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)

  class Meta:
    verbose_name_plural = 'Images'

  # def __str__(self):
  #   return self.image # X