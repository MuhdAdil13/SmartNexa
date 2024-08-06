from rest_framework import serializers
from .models import Customer  # Assuming you have a Customer model

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__' 

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = admin
        fields = '_all_'

