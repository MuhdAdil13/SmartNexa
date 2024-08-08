
from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1)
    address_1 = models.TextField()
    address_2 = models.TextField()

class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    employee_id = models.IntegerField()

class Seller(models.Model):
    seller_id = models.AutoField(primary_key=True)
    seller_name = models.CharField(max_length=255)
    legal_name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    alter_mobile = models.CharField(max_length=14)

class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    slug = models.TextField()
    categories = models.CharField(max_length=255)
    brand_name = models.CharField(max_length=100)
    images = models.ImageField()
    description = models.TextField()
    short_description = models.TextField()
   

class Inventory(models.Model):
    price = models.DecimalField(max_digits=7, decimal_places=2)
    original_price = models.DecimalField(max_digits=7, decimal_places=2)
    stock_quantity = models.IntegerField()

class Cart(models.Model):
    product_id = models.ForeignKey(Products,on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product_quantity = models.IntegerField()

    class Meta:
        unique_together = ('customer_id', 'product_id')

class Transaction(models.Model):
    transaction_id = models.CharField(primary_key=True,max_length=100)
    date = models.DateTimeField()
    payment_method = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    status = models.CharField(max_length=10)
    ip_address = models.CharField(max_length=35)
    response_code = models.IntegerField()
    response_message = models.CharField(max_length=100)

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    order_status = models.CharField(max_length=10)
    transaction_id = models.ForeignKey(Transaction,on_delete=models.CASCADE)

class OrderDetails(models.Model):
    order_details_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products,on_delete=models.CASCADE)
    product_quantity = models.IntegerField()
    total_amount = models.DecimalField(max_digits=7, decimal_places=2)
