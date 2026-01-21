from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Welcome to my first Django website ;-)!!!")

def about(request):
    return HttpResponse("About page")

def contact(request):
    return HttpResponse("Contact page")

def gallary(request):
    return HttpResponse("Gallary page")

def portfolio(request):
    return HttpResponse("Portfolio page")