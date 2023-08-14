from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index_adr, name="address"),
    path('add/', views.address_add, name="address_add"),
    path('edit/<int:pk>/', views.address_edit, name="address_edit"),
    path('del/<int:pk>/', views.address_del, name="address_del"),
]