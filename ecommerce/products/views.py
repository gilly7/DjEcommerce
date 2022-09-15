from django.views.generic import ListView
from products.models import Product
from django.shortcuts import render

# class Home(ListView):
#     model = Product
#     template_name = 'products/home.html'

def home(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'home.html',context) 
