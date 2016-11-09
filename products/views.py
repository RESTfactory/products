from rest_framework import viewsets
from .filters import ProvisionFilter
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
from .serializers import (
    BrandSerializer,
    CategorySerializer,
    ProductSerializer,
    ClientSerializer,
    ProductInstanceSerializer,
    LocalSerializer,
    ProvisionSerializer,
    ProductStatusSerializer,
    PriceTypeSerializer,
    ProductDataSerializer,
    PriceDataSerializer,
    PresenceDataSerializer,
    ShareDataSerializer
)

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ProductInstanceViewSet(viewsets.ModelViewSet):
    queryset = ProductInstance.objects.all()
    serializer_class = ProductInstanceSerializer

class LocalViewSet(viewsets.ModelViewSet):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer

class ProvisionViewSet(viewsets.ModelViewSet):
    queryset = Provision.objects.all()
    serializer_class = ProvisionSerializer
    # filter_class = ProvisionFilter

class ProductStatusViewSet(viewsets.ModelViewSet):
    queryset = ProductStatus.objects.all()
    serializer_class = ProductStatusSerializer

class PriceTypeViewSet(viewsets.ModelViewSet):
    queryset = PriceType.objects.all()
    serializer_class = PriceTypeSerializer

class ProductDataViewSet(viewsets.ModelViewSet):
    queryset = ProductData.objects.all()
    serializer_class = ProductDataSerializer

class PriceDataViewSet(viewsets.ModelViewSet):
    queryset = PriceData.objects.all()
    serializer_class = PriceDataSerializer

class PresenceDataViewSet(viewsets.ModelViewSet):
    queryset = PresenceData.objects.all()
    serializer_class = PresenceDataSerializer

class ShareDataViewSet(viewsets.ModelViewSet):
    queryset = ShareData.objects.all()
    serializer_class = ShareDataSerializer
