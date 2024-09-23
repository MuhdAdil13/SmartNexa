from django.urls import path
from .views import SellerRegisterView


urlpatterns=[
    path('/register',SellerRegisterView.as_view(),name="seller-register")
]

