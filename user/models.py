from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField()

    def __str__(self):
        return f'{self.user.username} Wallet'


