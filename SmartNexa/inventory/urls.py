from django.urls import path
from .views import InventoryView

urlpatterns = [
    path('/add_inventory', InventoryView.as_view(), name='add_inventory'),
]
