from rest_framework import serializers
from .models import Brand, Category, Product

class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brand

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
