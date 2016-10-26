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
    brand = BrandSerializer(many=False, read_only=False)
    category = CategorySerializer(many=False, read_only=False)

    class Meta:
        model = Product
        fields = [ "url", "id", "sku", "name", "image", "brand", "category"]

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = [ "url", "id", "name", "code"]

class ProductInstanceSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer(many=False, read_only=False)
    product = ProductSerializer(many=False, read_only=False)
    client = ClientSerializer(many=False, read_only=False)

    class Meta:
        model = ProductInstance
        fields = [ "url", "id", "name", "category", "product", "client"]

class LocalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Local
        fields = [ "url", "id", "name", "code", "place_id"]

class ProvisionSerializer(serializers.HyperlinkedModelSerializer):
    local = LocalSerializer(many=False, read_only=False)
    product_instances = ProductInstanceSerializer(many=True, read_only=False)

    class Meta:
        model = Provision
        fields = ["url", "id", "start_at", "end_at", "local", "product_instances"]

class ProductStatusSerializer(serializers.HyperlinkedModelSerializer):
    client = ClientSerializer(many=False, read_only=False)

    class Meta:
        model = ProductStatus
        fields = ["url", "id", "code", "name", "client"]

class ProductDataSerializer(serializers.HyperlinkedModelSerializer):
    product_instance = ProductInstanceSerializer(many=False, read_only=False)
    local = LocalSerializer(many=False, read_only=False)
    provision = ProvisionSerializer(many=False, read_only=False)
    status = ProductStatusSerializer(many=False, read_only=False)

    class Meta:
        model = ProductData
        fields = ["url", "id", "price", "shelf_share", "shelf_stock", "product_instance", "local", "provision", "status"]
