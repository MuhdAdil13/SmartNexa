from django.db import models
from sn_user.models import SmartNexaUser

# Create your models here.

class Seller(models.Model):
    user = models.OneToOneField(SmartNexaUser,on_delete=models.CASCADE,related_name='seller_profile')
    company_name=models.CharField(max_length=155)
    company_address=models.TextField()
    tax_id=models.CharField(max_length=100)

    def __str__(self):
        return self.company_name  #To Identifying object name 
