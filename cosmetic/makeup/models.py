from django.db import models
from datetime import datetime

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=25)
    orgin = models.CharField(max_length=25)
    logo = models.ImageField(upload_to ='logo/%Y/%m/%d/')

    def __str__(self):
        return self.name
    
    def get_absolute_url():
        pass

class Products(models.Model):
    name = models.CharField(max_length=25)
    kind = models.CharField(max_length=25)
    descreption = models.TextField(null=True)
    expir_date = models.DateField(null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.ImageField(upload_to ='photos/%Y/%m/%d/')
    is_active = models.BooleanField(default=True)
    publish_date = models.DateTimeField(default=datetime.now)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=False, default=None)
    
    def __str__(self):
        return self.name
    

    def get_absolute_url():
        pass