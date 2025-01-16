from django.shortcuts import render
from .models import Product


def product_page(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'category': product.category,
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'created_at': product.created_at,
        'updated_at': product.updated_at,
    }
    return render(request, 'catalog/product.html', context=context)


def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'catalog/home.html', context=context)


def contacts_page(request):
    return render(request, 'catalog/contacts.html')
