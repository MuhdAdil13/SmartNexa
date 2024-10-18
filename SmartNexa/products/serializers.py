from rest_framework import serializers
from .models import Product, Inventory
from django.utils import timezone

class ProductSerializer(serializers.ModelSerializer):
    discount_price = serializers.DecimalField(required=False, max_digits=7,decimal_places=2, min_value=0)
    # image = serializers.ImageField(required=False)

    class Meta:
        model = Product
        fields = (
            'name', 'price', 'discount_price', 'brand', 
            'category', 'connectivity', 'model_number', 
            'serial_number', 'short_description', 'description', 
            'slug','image', 'created_at', 'updated_at', 'is_enabled'
        )

    def create(self, validated_data):
        try:
            product = Product(
                name=validated_data['name'],
                price=validated_data['price'],
                discount_price=validated_data.get('discount_price', 0),
                brand=validated_data['brand'],
                category=validated_data['category'],
                connectivity=validated_data['connectivity'],
                model_number=validated_data['model_number'],
                serial_number=validated_data['serial_number'],
                short_description=validated_data.get('short_description', ''),
                description=validated_data.get('description', ''),
                slug=validated_data['slug'],
                image=validated_data['image'],
                created_at=validated_data.get('created_at', timezone.now()),
                updated_at=validated_data.get('updated_at', timezone.now()),
                is_enabled=validated_data.get('is_enabled', True)
            )
            product.save()
            return product
        except Exception as e:
            print(f"Validation Error: {e}")
            raise serializers.ValidationError(f"Error creating product: {e}")



class InventorySerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

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
        instance.stock_quantity = validated_data.get('stock_quantity', instance.stock_quantity)
        instance.restock_date = validated_data.get('restock_date', instance.restock_date)
        instance.save()
        return instance