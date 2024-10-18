from django.urls import path
from .views import ProductsView,InventoryView

urlpatterns = [
    path('/add_products',ProductsView.as_view(),name='add_products'),
    path('/add_inventory',ProductsView.as_view(),name='add_inventory')
]