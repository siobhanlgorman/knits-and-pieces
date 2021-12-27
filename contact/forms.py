from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=150, required=True)
    email_address = forms.EmailField(required=True)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Your Name',
            'email_address': 'Your Email Address',
            'subject': 'Subject',
            'message': 'Your Message',
        }

    class Meta:
        """Sets the fields for the contact form"""
        model = Contact
        fields = ('name', 'subject', 'email_address', 'message')
