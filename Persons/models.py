from django.db import models

# Create your models here.

class Persons(models.Model):
    name = models.CharField(max_length=255)
    family = models.CharField(max_length=255)
    email = models.CharField(max_length=400,null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
 

    def __str__(self):
        return f" {self.name}_{self.family} "   
    
from django.db import models

class FormEntry(models.Model):
    username = models.CharField(max_length=100, unique=True)  # نام کاربری یا شماره دستگاه
    has_filled_form = models.BooleanField(default=False)      # آیا فرم پر شده است یا خیر
