from django.contrib import admin
from .models import Category, Product, Order, ProductImage
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'description',)
    list_filter = ('category',)
    search_fields = ('name', 'category__name', 'description',)
    autocomplete_fields = ('category',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ( 'product', 'quantity', 'total_price', 'created_at',)
    list_filter = ('created_at',)
    search_fields = ( 'product__name',)

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ( 'product',)
    list_filter = ('product__name',)
    search_fields = ( 'product__name',)

# Register your models here.
