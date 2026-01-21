from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('event/', views.event, name='event'),
    path('menu/', views.menu, name='menu'),
    path('bill/', views.bill, name='bill'),
]