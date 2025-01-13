from django.contrib import admin
from django.urls import path

from  . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shop', views.shop, name='shop'),  # Shop page
    path('about', views.about, name='about'),  # About Us page
    path('contact', views.contact, name='contact') # Contact page
]


