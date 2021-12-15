"""Imports"""
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """override the ready method and import signals.py"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        import checkout.signals
