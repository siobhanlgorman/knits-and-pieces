from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to render the index page """
    return render(request, 'home/index.html')


def about(request):
    """ A view to render the about page """
    return render(request, 'home/about.html')


def privacy(request):
    """ A view to render the privacy policy page """
    return render(request, 'home/privacy.html')
