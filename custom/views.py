from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import CustomOrderForm


def custom(request):
    """ A view to return the custom order page"""
    if request.method == 'POST':
        form = CustomOrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Thanks for your message. We will be in touch with your quote shortly.')
            return redirect('custom')

    form = CustomOrderForm()
    context = {'form': form}
    return render(request, 'custom/custom.html', context)
