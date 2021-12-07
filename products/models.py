from django.db import models


class Category(models.Model):
    """A model for the product category"""
    name = models.CharField(max_length=80)
    friendly_name = models.CharField(max_length=80, blank=True, default="")

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name