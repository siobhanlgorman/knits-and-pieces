"""Imports"""
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from bag.contexts import bag_contents
from .forms import OrderForm

import stripe

def checkout(request):
    """
    Gets the contents of the shopping bag and
    calculate the total for stripe payments
    """
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your shopping basket is empty!")
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JuIr7COrUsI3DzkaimLXcFhEWD2xP0R3BTNeBjpY0JD8i74OomNsCuOChuOSFHJyQwN2ub3UZtWU086nQHcBfzX00AfcEkQZx',
        'client_secret': 'test client secret'

    }

    return render(request, template, context)
