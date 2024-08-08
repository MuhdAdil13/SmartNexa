from django.shortcuts import render,redirect
from django.http import HttpResponse as HR
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Admin
from ..serializers import AdminSerializer

class AdminViewSet(viewsets.ModelViewSet):
    queryset=Admin.objects.all()    
    serializer_class = AdminSerializer

@api_view(['GET','POST'])
def admin_list(request):
    """
      List all admins, or create new admin
    """
    if request.method == "GET":
        admins_data = Admin.objects.all()
        serializer=AdminSerializer(admins_data, many=True)
    
    elif request.method == "POST":
         serializer = AdminSerializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def admin_detail(request, pk):
    """
    Retrieve, update or delete a customer instance.
    """
    try:
        admin_data = Admin.objects.get(pk=pk)
    except Admin.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AdminSerializer(admin_data)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AdminSerializer(admin_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        admin_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)