from django.db import models
from products.models import Product

# Create your models here.


class Inventory(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='inventory')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=0)
    restock_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.product.name} - {self.quantity} in stock"
