from django.db import models

# Create your models here.
class Coin(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    def __str__(self):
        return f'Info[id={self.id}, name={self.name}, price={self.price}]'
