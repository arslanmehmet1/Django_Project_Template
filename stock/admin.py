from django.contrib import admin
from .models import Brand, Category, Product, Purchases, Sales, Firms

# Register your models here.
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Purchases)
admin.site.register(Sales)
admin.site.register(Firms)