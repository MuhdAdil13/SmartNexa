from rest_framework import serializers
from .models import *


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = admin
        fields = '_all_'


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = seller
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = '__all__'


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = inventory
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = cart
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = transaction
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = order
        fields = '__all__'


class OrDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = order_details
        fields = '__all__'
