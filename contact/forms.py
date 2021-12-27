from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=150, label="Your name")
    email_address = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Full Name',
            'email_address': 'Email Address',
            'message': 'Your Message',
        }

    class Meta:
        """Sets the fields for the contact form"""
        model = Contact
        fields = ('name', 'email_address', 'message')
