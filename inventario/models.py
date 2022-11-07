from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Productos(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    cost = models.IntegerField(default = 0)
    cantidad_stock = models.IntegerField(default = 0)
    description = models.TextField() 