"""Imports"""
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your shopping basket is empty!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JuIr7COrUsI3DzkaimLXcFhEWD2xP0R3BTNeBjpY0JD8i74OomNsCuOChuOSFHJyQwN2ub3UZtWU086nQHcBfzX00AfcEkQZx',
        'client_secret': 'test client secret'

    }

    return render(request, template, context)
