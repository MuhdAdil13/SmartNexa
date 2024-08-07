from django.shortcuts import render,redirect
from django.http import HttpResponse as HR
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Customer
from .serializers import CustomerSerializer
from .views.customer import *
