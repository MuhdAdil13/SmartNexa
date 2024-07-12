
from django.db import models

# Create your models here.
class customer(models.Model):
    cust_id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    gender=models.CharField(max_length=1)
    address_1=models.TextField()
    address_2=models.TextField()
    cart_id=models.IntegerField()

