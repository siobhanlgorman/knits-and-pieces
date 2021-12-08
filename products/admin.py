from django.contrib import admin
from .models import Product, Category, Tag

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'price',
        'image',
    )
class TagAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Tag)