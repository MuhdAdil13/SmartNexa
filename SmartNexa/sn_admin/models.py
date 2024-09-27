from django.db import models
from sn_user.models import SmartNexaUser

# Create your models here.

class Admin(models.Model):
    user = models.OneToOneField(SmartNexaUser,on_delete=models.CASCADE,related_name='admin_profile')
    role=models.CharField(max_length=155)
    
    def __str__(self):
        return self.user.firstname  #To Identifying object name 
