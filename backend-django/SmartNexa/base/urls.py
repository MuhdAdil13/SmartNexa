from django.urls import path,include
from base import views
from .views import CustomerViewSet


router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]