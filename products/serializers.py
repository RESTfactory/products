from rest_framework import serializers
from rest_framework_json_api.relations import ResourceRelatedField
from .models import (
    Brand,
    Category,
    Product,
    Client,
    ProductInstance,
    Local,
    Provision,
    ProductStatus,
    PriceType,
    ProductData,
    PriceData,
    PresenceData,
    ShareData
)

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["url", "id", "name"]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [ "url", "id", "name", "code", "description"]

class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(many=False, read_only=False)
    category = CategorySerializer(many=False, read_only=False)

    class Meta:
        model = Product
        fields = [ "url", "id", "sku", "name", "image", "brand", "category"]

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [ "url", "id", "name", "code"]

class ProductInstanceSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False, read_only=False)
    product = ProductSerializer(many=False, read_only=False)
    client = ClientSerializer(many=False, read_only=False)

    class Meta:
        model = ProductInstance
        fields = [ "url", "id", "code", "name", "category", "product", "client"]

class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = [ "url", "id", "name", "code", "place_id"]

class ProvisionSerializer(serializers.ModelSerializer):
    local = LocalSerializer(many=False, read_only=False)
    product_instances = ProductInstanceSerializer(many=True, read_only=False)

    class Meta:
        model = Provision
        fields = ["url", "id", "start_at", "end_at", "local", "product_instances"]

class ProductStatusSerializer(serializers.ModelSerializer):
    client = ClientSerializer(many=False, read_only=False)

    class Meta:
        model = ProductStatus
        fields = ["url", "id", "code", "name", "client"]

class PriceTypeSerializer(serializers.ModelSerializer):
    # client = ClientSerializer(many=False, read_only=True)

    class Meta:
        model = PriceType
        fields = ["url", "id", "code", "name", "client"]

class ProductDataMixinSerializer(serializers.ModelSerializer):
    # product_instance = ProductInstanceSerializer(many=False, read_only=False)
    # local = LocalSerializer(many=False, read_only=False)
    # provision = ProvisionSerializer(many=False, read_only=False)
    pass

#TODO: Delete
class ProductDataSerializer(ProductDataMixinSerializer):
    status = ProductStatusSerializer(many=False, read_only=False)

    class Meta:
        model = ProductData
        fields = ["url", "id", "price", "shelf_share", "shelf_stock", "product_instance", "local", "provision", "status"]

class PriceDataSerializer(ProductDataMixinSerializer):

    class Meta:
        model = PriceData
        fields = ["url", "id", "price", "price_type", "product_instance", "local", "provision"]

class PresenceDataSerializer(ProductDataMixinSerializer):

    class Meta:
        model = PresenceData
        fields = ["url", "id", "status", "product_instance", "local", "provision"]

class ShareDataSerializer(ProductDataMixinSerializer):

    class Meta:
        model = ShareData
        fields = ["url", "id", "shelf_share", "shelf_stock", "product_instance", "local", "provision"]
