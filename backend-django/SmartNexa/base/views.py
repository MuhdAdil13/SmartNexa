from django.shortcuts import render,redirect
from django.http import HttpResponse as HR

# Create your views here.
def display(request):
    return HR("Welcome Back")