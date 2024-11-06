from django.db import models
from products.models import Product

# Create your models here.


class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='inventory')
    stock_quantity = models.PositiveIntegerField(default=0)
    quantity_sold = models.PositiveIntegerField(default=0)
    quantity_returned = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def update_inventory(self, quantity_sold):
        self.quantity_in_stock -= quantity_sold
        self.quantity_sold += quantity_sold
        self.save()

    def __str__(self):
        return f"{self.product.name} - {self.quantity} in stock"
