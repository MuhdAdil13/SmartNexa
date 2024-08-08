from django.shortcuts import render, redirect
from django.http import HttpResponse as HR
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import inventory
from .serializers import InventorySerializer


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = inventory.objects.all()
    serializer_class = InventorySerializer


@api_view(['GET', 'POST'])
def inventory_list(request):
    """
    List all inventory details, or add details.
    """
    if request.method == 'GET':
        inventory_data = inventory.objects.all()
        serializer = InventorySerializer(inventory_data, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = InventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def inventory_detail(request, pk):
    """
    Retrieve, update or delete a product instance.
    """
    try:
        inventory_data = inventory.objects.get(pk=pk)
    except inventory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InventorySerializer(inventory_data)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = InventorySerializer(inventory_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        inventory_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
