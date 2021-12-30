from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Fields to display in admin panel"""

    list_display = ('name', 'email_address', 'subject')