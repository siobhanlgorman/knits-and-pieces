from django.shortcuts import render


def custom(request):
    """ A view to return the custom order page"""

    return render(request, 'custom/custom.html')
