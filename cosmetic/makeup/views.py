from multiprocessing import context
import django
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    context = {
        "Brand": Brand.objects.all(),
        "Products": Products.objects.all(),
    }
    return render(request, 'makeup/index.html', context)