"""Imports"""
from django import forms
from .models import CustomOrder


class CustomOrderForm(forms.ModelForm):
    """Sets fields and placeholder"""

    message = forms.CharField(
        required=False, widget=forms.Textarea(
            attrs={'placeholder': 'Any additional information'}))

    class Meta:
        """Sets the fields for the contact form"""
        model = CustomOrder
        fields = '__all__'
