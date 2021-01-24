from django.contrib import admin
from .models import Product, ProductCategory, ProductImage, ProductCollection


class ProductImageStackedAdmin(admin.StackedInline):
    model = ProductImage

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ['price_final']
    inlines = [ProductImageStackedAdmin]
    search_fields = ['name']

@admin.register(ProductCollection)
class ProductCollectionAdmin(admin.ModelAdmin):
    autocomplete_fields = ['collection']
    search_fields = ['name']
    readonly_fields = ['slug']


