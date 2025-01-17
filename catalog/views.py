from .models import Product
from django.views.generic import DetailView, ListView, TemplateView


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'


class ProductTemplateView(TemplateView):
    model = Product
    template_name = "catalog/contacts.html"
