from django import forms
from logging import PlaceHolder
from django.core.validators import MinValueValidator
from .models import Products
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from datetime import datetime

# Create your forms here.

class ProductsForm(forms.Form):

    name=forms.CharField(label='name',max_length=50)
    kind=forms.CharField(label='kind',max_length=50)
    descreption=forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))
    expir_date=forms.DateField(label='expir_date')
    price=forms.IntegerField(label='price')
    photo = forms.ImageField(upload_to ='photos/%Y/%m/%d/')
    is_active = forms.BooleanField(label='active', default=True)
    publish_date = forms.DateTimeField(default=datetime.now)
    brand=forms.IntegerField(label='brand')
    
    def save(self, id=None):
        
        name = self.cleaned_data['name']
        kind = self.cleaned_data['kind']
        descreption = self.cleaned_data['descreption']
        expir_date = self.cleaned_data['expir_date']
        price = self.cleaned_data['price']
        photo = self.cleaned_data['photo']
        is_active = self.cleaned_data['is_active']
        publish_date = self.cleaned_data['publish_date']
        brand = self.cleaned_data['brand']

        return Products.objects.create(name=name,kind=kind,descreption=descreption,expir_date=expir_date,price=price,brand=brand)
        


    def update(self, Products=None):
        Products.name = self.cleaned_data['name']
        Products.kind = self.cleaned_data['kind']
        Products.descreption = self.cleaned_data['descreption']
        Products.expir_date = self.cleaned_data['expir_date']
        Products.price = self.cleaned_data['price']
        Products.photo = self.cleaned_data['photo']
        Products.is_active = self.cleaned_data['is_active']
        Products.publish_date = self.cleaned_data['publish_date']
        Products.brand = self.cleaned_data['brand']
        Products.save()