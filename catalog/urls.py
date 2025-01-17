from django.urls import path

from .apps import CatalogConfig
from .views import ProductListView, ProductDetailView, ProductTemplateView

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', ProductTemplateView.as_view(), name='contacts'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('home/', ProductListView.as_view(), name='product_list'),
]
