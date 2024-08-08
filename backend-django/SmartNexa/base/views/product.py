from django.shortcuts import render, redirect
from django.http import HttpResponse as HR
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import products
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = products.objects.all()
    serializer_class = ProductSerializer


@api_view(['GET', 'POST'])
def product_list(request):
    """
    List all products, or add a product.
    """
    if request.method == 'GET':
        products_data = products.objects.all()
        serializer = ProductSerializer(products_data, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    """
    Retrieve, update or delete a product instance.
    """
    try:
        product_data = products.objects.get(pk=pk)
    except products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product_data)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductSerializer(product_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
