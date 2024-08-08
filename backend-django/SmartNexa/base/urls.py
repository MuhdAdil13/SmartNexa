from django.urls import path,include
from base import views
from .apiViews.customer import CustomerViewSet
from .apiViews.admin import AdminViewSet
from .apiViews.seller import SellerViewSet
from .apiViews.product import ProductViewSet
from .apiViews.inventory import InventoryViewSet
from .apiViews.cart import CartViewSet
from .apiViews.transaction import TransactionViewSet
from .apiViews.order import OrderViewSet
from .apiViews.order_details import OrderDetailsViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'admin', AdminViewSet)
router.register(r'seller', SellerViewSet)
router.register(r'products', ProductViewSet)
router.register(r'inventory', InventoryViewSet)
router.register(r'cart', CartViewSet)
router.register(r'transaction', TransactionViewSet)
router.register(r'order', OrderViewSet)
router.register(r'order_details', OrderDetailsViewSet)

urlpatterns = [
    path('', include(router.urls))
]

