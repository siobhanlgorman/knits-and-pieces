from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Your name'}))
    email_address = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'Your email'}))
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Your message'}))

    class Meta:
        """Sets the fields for the contact form"""
        model = Contact
        fields = '__all__'
