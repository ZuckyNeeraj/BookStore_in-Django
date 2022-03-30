from django.db import models

# Create your models here.


class Products(models.Model):
    product_name = models.CharField(max_length=300)
    product_desc = models.TextField(max_length=1000)
    product_price = models.FloatField()
    product_discount_price = models.FloatField()
    product_category = models.CharField(max_length=200)
    product_image = models.CharField(max_length=300)
