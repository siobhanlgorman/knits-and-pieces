"""Imports"""
from django import forms
from .models import CustomOrder, Product


class CustomOrderForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Your name'}))
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'Your email'}))
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Your message'}))
    size = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Size'}))
    material = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Material'}))
    design = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Design Name'}))
    colour1 = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Main Colour'}))
    colour2 = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Second Colour'}))
    colour3 = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Third Colour'}))
    colour4 = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Fourth Colour'}))


    class Meta:
        """Sets the fields for the contact form"""
        model = CustomOrder
        fields = '__all__'
