from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

def product_list(request):
    products = Product.objects.filter(is_active=True)  # Only display active products
    return render(request, 'index.html', {'products': products})


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect back to the product list
    else:
        form = ProductForm()
    return render(request, 'product_create.html', {'form': form})
