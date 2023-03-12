from django.db import models


class Product(models.Model):
    art = models.IntegerField(null=True)
    brand = models.CharField(max_length=50, null=True)
    model = models.CharField(max_length=50, null=True)
    type = models.CharField(max_length=50, null=True)
    year_of_origin = models.IntegerField(null=True)
    description = models.CharField(max_length=200, null=True)
    is_prod = models.CharField(max_length=50, null=True)
    engine = models.CharField(max_length=50, null=True)
    torque = models.CharField(max_length=50, null=True)
    gearbox = models.CharField(max_length=50, null=True)
    drive = models.CharField(max_length=50, null=True)
    color = models.CharField(max_length=50, null=True)
    mileage = models.CharField(max_length=50, null=True)
    hand = models.CharField(max_length=50, null=True)
    fueltank = models.IntegerField(null=True)
    fuelecon = models.CharField(max_length=50, null=True)
    price = models.IntegerField(null=True)
    image = models.ImageField(upload_to='static/images/collection')

class ProductImage(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='static/images/collection')

class ProductPoint(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=True)
    address = models.CharField(max_length=300, null=True)
    phonenumber = models.CharField(max_length=100, null=True)

class Brand(models.Model):
    art = models.IntegerField()
    brand = models.CharField(max_length=50)
    img = models.ImageField(upload_to='static/images/clients', null=True)

class TopModel(models.Model):
    art = models.IntegerField()
    brand = models.CharField(max_length=50, null=True)
    model = models.CharField(max_length=50, null=True)
    type = models.CharField(max_length=50, null=True)
    description1 = models.CharField(max_length=400, null=True)
    description2 = models.CharField(max_length=400, null=True)
    description3 = models.CharField(max_length=400, null=True)
    image = models.ImageField(upload_to='static/images/collection')

class BlogPost(models.Model):
    art = models.IntegerField()
    name = models.CharField(max_length=100, null=True)
    author = models.CharField(max_length=50, null=True)
    date = models.CharField(max_length=50, null=True)
    maindesc = models.CharField(max_length=400, null=True)
    mainimg = models.ImageField(upload_to='static/images/blog', null=True)
    title1 = models.CharField(max_length=80, null=True)
    desc1 = models.CharField(max_length=8000, null=True)
    img1 = models.ImageField(upload_to='static/images/blog')
    title2 = models.CharField(max_length=80, null=True)
    desc2 = models.CharField(max_length=8000, null=True)
    img2 = models.ImageField(upload_to='static/images/blog')
    title3 = models.CharField(max_length=80, null=True)
    desc3 = models.CharField(max_length=8000, null=True)
    img3 = models.ImageField(upload_to='static/images/blog')
    finaldesc = models.CharField(max_length=8000, null=True)


