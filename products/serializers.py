from rest_framework import serializers
from .models import Brand, Category, Product, Client, ProductInstance, Local, Provision, ProductStatus, ProductData

class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brand

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client

class ProductInstanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductInstance

class LocalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Local

class ProvisionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Provision

class ProductStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductStatus

class ProductDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductData
