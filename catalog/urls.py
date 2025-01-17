from django.urls import path

from .apps import CatalogConfig
from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', views.contacts_page, name='contacts'),
    path('product/<int:pk>/', views.product_page, name='product'),
    path('home/', views.product_list, name='home'),
]
