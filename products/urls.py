"""products URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from .views import (
    BrandViewSet,
    CategoryViewSet,
    ProductViewSet,
    ProductInstanceViewSet,
    LocalViewSet,
    ProvisionViewSet,
    ProductStatusViewSet,
    PriceTypeViewSet,
    PriceDataViewSet,
    PresenceDataViewSet,
    ShareDataViewSet
)

router = routers.DefaultRouter()
router.register(r'brands', BrandViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'productsinstances', ProductInstanceViewSet)
router.register(r'locals', LocalViewSet)
router.register(r'provisions', ProvisionViewSet)
router.register(r'productstatus', ProductStatusViewSet)
router.register(r'pricetypes', PriceTypeViewSet)
router.register(r'pricedatas', PriceDataViewSet)
router.register(r'presencedatas', PresenceDataViewSet)
router.register(r'sharedatas', ShareDataViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
