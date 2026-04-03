from django.shortcuts import render,redirect
from .models import product
from .forms import ProductForm

# Create your views here.
def product_list(request):
    products = product.objects.all()
    return render(request, 'Product/product_list.html', {'products': products})

def product_add(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'Product/product_form.html', {'form': form})

def product_update(request, id):
    productItem = product.objects.get(id=id)
    form = ProductForm(instance=productItem)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=productItem)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'Product/product_form.html', {'form': form})

def product_delete(request, id):
    productItem = product.objects.get(id=id)
    if request.method == "POST":
        productItem.delete()
        return redirect('product_list')
    return render(request, 'Product/product_delete.html', {'product': product})