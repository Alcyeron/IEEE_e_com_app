from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.TextField()
    details = models.TextField()
    image = models.URLField()
    rating = models.FloatField()
    price = models.IntegerField()
    mrp = models.IntegerField()
    quantity = models.IntegerField(default=10)

    def __str__(self):
        return self.name
