# from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from .serializers import AdminRegisterSerializer


# Create your views here.
class AdminRegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        serializer=AdminRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)