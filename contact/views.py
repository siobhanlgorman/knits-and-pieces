from django.shortcuts import render

from .forms import ContactForm

def contact(request):
    """ A view to return the contact page"""

    return render(request, 'contact/contact.html')
