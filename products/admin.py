from django.contrib import admin
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
    PriceData,
    PresenceData,
    ShareData
)

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Client)
admin.site.register(ProductInstance)
admin.site.register(Local)
admin.site.register(Provision)
admin.site.register(ProductStatus)
admin.site.register(PriceType)
admin.site.register(PriceData)
admin.site.register(PresenceData)
admin.site.register(ShareData)
