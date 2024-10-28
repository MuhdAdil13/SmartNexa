from rest_framework import serializers
from products.models import Product
from .models import Inventory
from django.utils import timezone


class InventorySerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all())

    class Meta:
        model = Inventory
        fields = ['product', 'price', 'stock_quantity', 'restock_date']

    def create(self, validated_data):
        # Create an Inventory instance
        inventory = Inventory(
            product=validated_data['product'],
            price=validated_data['price'],
            stock_quantity=validated_data['stock_quantity'],
            restock_date=validated_data.get('restock_date')  # Optional field
        )
        inventory.save()
        return inventory

    def update(self, instance, validated_data):
        # Update an existing Inventory instance
        instance.price = validated_data.get('price', instance.price)
        instance.stock_quantity = validated_data.get(
            'stock_quantity', instance.stock_quantity)
        instance.restock_date = validated_data.get(
            'restock_date', instance.restock_date)
        instance.save()
        return instance
