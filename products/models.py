from django.conf import settings
from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=30)
    description = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    sku = models.CharField(max_length=40, unique=True)
    name = models.CharField(max_length=30)
    brand = models.ForeignKey(Brand, blank=True)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name
