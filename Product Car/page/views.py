from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.filter(is_active=True)  # Only display active products
    return render(request, 'index.html', {'products': products})
