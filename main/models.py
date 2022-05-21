from django.db import models


class Product(models.Model):
    art= models.IntegerField()
    name_product = models.CharField(max_length=50)
    price = models.IntegerField()
    creator_id = models.IntegerField()
    year = models.IntegerField()
    category_id = models.IntegerField()
    amount = models.IntegerField()
    availability = models.CharField(max_length=50)
    img = models.ImageField(upload_to='static/images')


class Category(models.Model):
    name_category = models.CharField(max_length=50)


class Creator(models.Model):
    name_creator = models.CharField(max_length=50)
    country_creator = models.CharField(max_length=50)
