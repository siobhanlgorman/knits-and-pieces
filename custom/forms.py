"""Imports"""
from django import forms
from .models import CustomOrder


class CustomOrderForm(forms.ModelForm):

    class Meta:
        """Sets the fields for the contact form"""
        model = CustomOrder
        fields = '__all__'
