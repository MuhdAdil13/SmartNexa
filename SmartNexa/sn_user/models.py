from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


class SmartNexaUserManager(BaseUserManager):
    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError("User Must have an Email Address")
        user = self.model(email=self.normalize_email(email),**extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user
        
    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_superuser',True)
        return self.create_user(email,password,**extra_fields)


class SmartNexaUser(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField(unique=True)  # Ensure email is unique
    mobile = models.CharField(max_length=15, blank=True, null=True)  # Optional mobile field
    is_active = models.BooleanField(default=True)
    user_type = models.CharField(max_length=20)
    is_superuser = models.BooleanField(default=False)
    objects = SmartNexaUserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['firstname','lastname','mobile']
    
    def __str__(self):
        return self.username
    

