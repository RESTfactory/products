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
    name = models.CharField(max_length=100)
    image = models.URLField(max_length=255, blank=True)
    brand = models.ForeignKey(Brand, blank=True, null=True)
    category = models.ForeignKey(Category, blank=True, null=True)

    def __str__(self):
        return self.name

#Provisional model
class Client(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name


class ProductInstance(models.Model):
    code = models.CharField(max_length=40, blank=True, null=True)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, blank=True, null=True)
    product = models.ForeignKey(Product, blank=True)
    client = models.ForeignKey(Client, blank=True, null=True)

    def __str__(self):
        return self.name

class Local(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=40, unique=True, primary_key=True)
    local_code = models.CharField(max_length=40)
    place_id = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name

class Provision(models.Model):
    product_instances = models.ManyToManyField(ProductInstance)
    local = models.ForeignKey(Local)

    start_at = models.DateTimeField(auto_now_add=True)
    end_at = models.DateTimeField()

    def __str__(self):
        return str(self.id)

class ProductStatus(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    client = models.ForeignKey(Client, blank=True, null=True)

    def __str__(self):
        return self.name

class PriceType(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    client = models.ForeignKey(Client, blank=True, null=True)

    def __str__(self):
        return self.name

class ProductDataMixin(models.Model):
    product_instance = models.ForeignKey(ProductInstance)
    local = models.ForeignKey(Local)
    provision = models.ForeignKey(Provision, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class PriceData(ProductDataMixin):
    price = models.FloatField()
    price_type = models.ForeignKey(PriceType)

    def __str__(self):
        return str(self.id)

class PresenceData(ProductDataMixin):
    status = models.ForeignKey(ProductStatus)

    def __str__(self):
        return str(self.id)

class ShareData(ProductDataMixin):
    shelf_share = models.IntegerField()
    shelf_stock = models.IntegerField()

    def __str__(self):
        return str(self.id)
