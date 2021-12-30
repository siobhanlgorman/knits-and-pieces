from django.contrib import admin
from .models import CustomOrder


@admin.register(CustomOrder)
class CustomOrderAdmin(admin.ModelAdmin):
    """Fields to display in admin panel"""

    list_display = ('date_sent', 'name', 'email')
