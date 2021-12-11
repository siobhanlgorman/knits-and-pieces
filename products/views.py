"""Imports"""
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Tag
# Create your views here.


def all_products(request):
    """ A view to show all products including search and sort queries.
    Variables defined as None to display when no sorting or filtering """

    products = Product.objects.all()
    query = None
    categories = None
    tags = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'tag' in request.GET:
            tags = request.GET['tag'].split(',')
            products = products.filter(tag__name__in=tags)
            tags = Tag.objects.filter(name__in=tags)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter your search query!")
                return redirect(reverse('products'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show the product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)
