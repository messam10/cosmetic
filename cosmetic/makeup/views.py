from multiprocessing import context
import django
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import ProductsForm
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "Brand": Brand.objects.all(),
        "Products": Products.objects.all(),
    }
    return render(request, 'makeup/index.html', context)

def productDetail(request, pro_id):
    context = {
        "Pro": get_object_or_404(Products, pk = pro_id),
    }
    return render(request, 'makeup/products_details.html', context)

def add_Product(request):
	if request.method == "POST":
		products_form = ProductsForm(request.POST, request.FILES)
		if products_form.is_valid():
			products_form.save()
			messages.success(request, ('Your Product was successfully added!'))
		else:
			messages.error(request, 'Error saving form')
		
		
		return redirect("main:homepage")
	products_form = ProductsForm()
	product = Products.objects.all()
	return render(request=request, template_name="makeup/AddProsuct.html", context={'products_form':products_form, 'product':product})
