from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()
    image = models.ImageField(null=True)
    rating = models.FloatField()
    price = models.IntegerField()
    mrp = models.IntegerField()
    quantity = models.IntegerField(default=10)

    def __str__(self):
        return self.name
