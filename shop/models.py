from django.db import models
from PIL import Image
from django.contrib.auth.models import User


# Create your models here.


class Product(models.Model):
    id = models.CharField(primary_key=True, max_length=4)
    name = models.CharField(max_length=100)
    details = models.TextField()
    image = models.ImageField(null=True)
    rating = models.FloatField()
    price = models.IntegerField()
    mrp = models.IntegerField()
    quantity = models.IntegerField(default=10)

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 348 or img.width > 348:
            img.thumbnail((348, 348))
            img.save(self.image.path)


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.user} : {self.product} ({self.quantity})'
