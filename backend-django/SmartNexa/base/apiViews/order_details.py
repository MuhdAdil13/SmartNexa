from django.shortcuts import render, redirect
from django.http import HttpResponse as HR
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import OrderDetails
from ..serializers import OrDetailSerializer


class OrderDetailsViewSet(viewsets.ModelViewSet):
    queryset = OrderDetails.objects.all()
    serializer_class = OrDetailSerializer


@api_view(['GET', 'POST'])
def order_details_list(request):
    """
    List all order_details details, or add order_details.
    """
    if request.method == 'GET':
        order_details_data = OrderDetails.objects.all()
        serializer = OrDetailSerializer(order_details_data, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OrDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def order_info_detail(request, pk):
    """
    Retrieve, update or delete a order_details instance.
    """
    try:
        order_detail_data = OrderDetails.objects.get(pk=pk)
    except OrderDetails.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrDetailSerializer(order_detail_data)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OrDetailSerializer(order_detail_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        order_detail_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
