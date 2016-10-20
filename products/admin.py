from django.contrib import admin
from .models import Brand, Category, Product, Client, ProductInstance, Local, ProductData

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Client)
admin.site.register(ProductInstance)
admin.site.register(Local)
admin.site.register(ProductData)
