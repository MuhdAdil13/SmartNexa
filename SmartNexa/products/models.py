from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=100)
    category = models.CharField(max_length=100)  # e.g., "Smart watch", "Analog watch"
    image = models.ImageField(upload_to='images/')
    short_description = models.TextField(blank=True)
    description = models.TextField(blank=True)
    slug = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    connectivity = models.CharField(max_length=50, choices=[('WiFi', 'WiFi'), ('Bluetooth', 'Bluetooth')])
    model_number = models.CharField(max_length=100, unique=True)
    serial_number = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='inventory')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=0)
    restock_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.product.name} - {self.quantity} in stock"