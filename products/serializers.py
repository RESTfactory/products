from rest_framework import serializers
from rest_framework_json_api.relations import ResourceRelatedField
from .models import Brand, Category, Product, Client, ProductInstance, Local, Provision, ProductStatus, ProductData

class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brand
        fields = ["url", "id", "name"]

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = [ "url", "id", "name", "code", "description"]

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = [ "url", "id", "sku", "name", "brand", "category"]

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = [ "url", "id", "name", "code"]

class ProductInstanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductInstance
        fields = [ "url", "id", "name", "category", "product", "client"]

class LocalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Local
        fields = [ "url", "id", "name", "code", "place_id"]

class ProvisionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Provision
        fields = ["url", "id", "start_at", "end_at", "local", "product_instances"]

class ProductStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductStatus
        fields = ["url", "id", "code", "name", "client"]

class ProductDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductData
        fields = ["url", "id", "price", "shelf_share", "shelf_stock", "product_instance", "local", "provision", "status"]
