from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContactForm


def contact(request):
    """ A view to return the contact page"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Thanks for your message. We will be in touch soon.')
            return redirect('contact')

    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)
