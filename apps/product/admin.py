from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "size",  "stock", "image")
    fieldsets = ((None, {"fields": ("name", "price", "size",  "stock", "image")}),)

admin.site.register(Product, ProductAdmin)
