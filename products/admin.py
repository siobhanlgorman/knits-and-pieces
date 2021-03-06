"""Imports"""
from django.contrib import admin
from .models import Product, Category, Tag

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    """Lists product fields to be displayed in admin panel"""
    list_display = (
        'name',
        'category',
        'price',
        'image1',
    )


class CategoryAdmin(admin.ModelAdmin):
    """Lists category fields to be displayed in admin panel"""
    list_display = (
        'id',
        'friendly_name',
        'name',
    )


class TagAdmin(admin.ModelAdmin):
    """Lists tag fields to be displayed in admin panel"""
    list_display = (
        'name',
        'friendly_name',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Tag, TagAdmin)
