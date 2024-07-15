
from django.db import models

# Create your models here.


class customer(models.Model):
    cust_id = models.AutoField(primary_key=True)
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


class order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    order_date = models.DateTimeField()
    order_status = models.CharField(max_length=10)
    transaction_id = models.IntegerField()


class order_details(models.Model):
    order_details_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    product_id = models.IntegerField()
    product_quantity = models.IntegerField()
    total_amount = models.DecimalField(7, 2)


class cart(models.Model):
    product_id = models.IntegerField()
    customer_id = models.IntegerField()
    product_quantity = models.IntegerField()

    class Meta:
        unique_together = ('customer_id', 'product_id')


class products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    categories = models.CharField(max_length=255)
    brand_name = models.CharField(max_length=100)
    images = models.ImageField()


class inventory(models.Model):
    price = models.DecimalField(7, 2)
    original_price = models.DecimalField(7, 2)
    stock_quantity = models.IntegerField()
    is_in_stock = models.CharField(max_length=10)


class transaction(models.Model):
    transaction_id = models.AutoField()
    date = models.DateTimeField()
    payment_method = models.CharField()
    amount = models.DecimalField(7, 2)
    status = models.CharField(max_length=10)
    ip_address = models.DecimalField(20, 10)
    response_code = models.IntegerField()
    response_message = models.CharField(max_length=100)
