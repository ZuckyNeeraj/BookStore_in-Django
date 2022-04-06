from django.db import models

# Create your models here.


class Products(models.Model):
    product_name = models.CharField(max_length=300)
    product_desc = models.TextField(max_length=1000)
    product_price = models.FloatField()
    product_discount_price = models.FloatField()
    product_category = models.CharField(max_length=200)
    product_image = models.CharField(max_length=300)


class Order(models.Model):
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    total = models.CharField(max_length=200)
