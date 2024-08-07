from django.shortcuts import render,redirect
from django.http import HttpResponse as HR
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import cart
from .serializers import CartSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = cart.objects.all()
    serializer_class = CartSerializer

@api_view(['GET', 'POST'])
def product_list(request):
    """
    List all cart_details, or add cart details.
    """
    if request.method == 'GET':
        cart_data = cart.objects.all()
        serializer = ProductSerializer(cart_data, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def cart_detail(request, pk):
    """
    Retrieve, update or delete a cart details instance.
    """
    try:
        cart_data = cart.objects.get(pk=pk)
    except cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CartSerializer(product_data)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CartSerializer(cart_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cart_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)