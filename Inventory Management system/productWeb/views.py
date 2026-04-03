from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product
from .forms import ProductForm

def home(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'productWeb/home.html', context)

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Product '{form.cleaned_data['name']}' added successfully!")
            return redirect('home')
    else:
        form = ProductForm()
    
    return render(request, 'productWeb/add_product.html', {'form': form})

def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f"Product '{form.cleaned_data['name']}' updated successfully!")
            return redirect('home')
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'productWeb/edit_product.html', {'form': form, 'product': product})

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, f"Product '{product.name}' deleted successfully!")
        return redirect('home')
    return render(request, 'productWeb/delete_product.html', {'product': product})