from django.contrib import admin
from .models import Product, Category, Tag

# Register your models here.
admin.site.register(Product)
admin.site.register(Categry)
admin.site.register(Tag)