from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   
    path('',views.home),
    path('save/',views.save),
    path('show/',views.show),
    path('delete/',views.delete),
    path('edit/',views.edit),
    path('edited/',views.edited),
]
