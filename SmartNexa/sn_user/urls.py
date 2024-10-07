from django.urls import path
from .views import RegisterView,LoginView,LoginVerify
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns=[
    path('/login',LoginView.as_view(),name='login'),
    path('api/token/refresh',TokenRefreshView.as_view(),name='token_refresh'),
    path('/register',RegisterView.as_view(),name='register'),
    path('/verify',LoginVerify.as_view(),name='verify')
]
