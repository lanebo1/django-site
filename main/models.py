from django.db import models


class Product(models.Model):
    art = models.IntegerField()
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    amount = models.IntegerField()
    availability = models.CharField(max_length=50)
    image = models.ImageField(upload_to='static/images')
