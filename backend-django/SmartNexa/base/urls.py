from django.urls import path,include
from base import views
from .views import CustomerViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'customers', CustomerViewSet)

urlpatterns = [
    path('', include(router.urls))
]

