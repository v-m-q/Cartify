from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=50)

  class Meta:
    verbose_name_plural = 'Categories'

  def _str_(self):
    return self.name