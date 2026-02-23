from django.db import models

# Create your models here.
class Product(models.Model):
    ProductName = models.CharField(max_length=100)
    Quantity = models.IntegerField()
    Price = models.FloatField()
    Description = models.TextField()

    def __str__(self):
        return self.ProductName


