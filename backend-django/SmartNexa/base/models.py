
from django.db import models

# Create your models here.

class customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1)
    address_1 = models.TextField()
    address_2 = models.TextField()

class admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    employee_id = models.IntegerField()

class seller(models.Model):
    seller_id = models.AutoField(primary_key=True)
    seller_name = models.CharField(max_length=255)
    legal_name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    alter_mobile = models.CharField(max_length=14)

class products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    slug = models.TextField()
    categories = models.CharField(max_length=255)
    brand_name = models.CharField(max_length=100)
    images = models.ImageField()
    description = models.TextField()
    short_description = models.TextField()
   

class inventory(models.Model):
    price = models.DecimalField(max_digits=7, decimal_places=2)
    original_price = models.DecimalField(max_digits=7, decimal_places=2)
    stock_quantity = models.IntegerField()

class cart(models.Model):
    product_id = models.ForeignKey(products,on_delete=models.CASCADE)
    customer_id = models.ForeignKey(customer,on_delete=models.CASCADE)
    product_quantity = models.IntegerField()

    class Meta:
        unique_together = ('customer_id', 'product_id')

class transaction(models.Model):
    transaction_id = models.CharField(primary_key=True,max_length=100)
    date = models.DateTimeField()
    payment_method = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    status = models.CharField(max_length=10)
    ip_address = models.CharField(max_length=35)
    response_code = models.IntegerField()
    response_message = models.CharField(max_length=100)

class order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(customer,on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    order_status = models.CharField(max_length=10)
    transaction_id = models.ForeignKey(transaction,on_delete=models.CASCADE)

class order_details(models.Model):
    order_details_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(order,on_delete=models.CASCADE)
    product_id = models.ForeignKey(products,on_delete=models.CASCADE)
    product_quantity = models.IntegerField()
    total_amount = models.DecimalField(max_digits=7, decimal_places=2)
