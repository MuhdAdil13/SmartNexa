from django.urls import path
from .views import ProductsView

urlpatterns = [
    path('/add_products', ProductsView.as_view(), name='add_products'),
]
