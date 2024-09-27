from django.db import models
from sn_user.models import SmartNexaUser

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(SmartNexaUser,on_delete=models.CASCADE,related_name='customer_profile')
    gender=models.CharField(max_length=10)
    address_1=models.TextField(max_length=255)
    address_2=models.TextField(max_length=255)
    
    def __str__(self):
        return self.firstname  #To Identifying object name 
