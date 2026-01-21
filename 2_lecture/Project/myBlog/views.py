from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'myBlog/home.html')

def about(request):
    return render(request, 'myBlog/about.html')

def contact(request):
    return render(request, 'myBlog/contact.html')

def gallry(request):
    return render(request, 'myBlog/gallary.html')

def portfolio(request):
    return render(request, 'myBlog/portfolio.html')