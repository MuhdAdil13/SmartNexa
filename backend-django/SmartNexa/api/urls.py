from django.urls import path
from . import views

urlpatterns = [
    path('smartnexa',views.getData),
] 