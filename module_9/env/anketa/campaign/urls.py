from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="campaign"),
    path('add/', views.campaign_add, name='campaign_add'),
    path('view/<int:pk>/', views.campaign_view, name='campaign_view'),
    path('edit/<int:pk>/', views.campaign_edit, name='campaign_edit'),
    path('del/<int:pk>/', views.campaign_del, name='campaign_del'),
    path('address_add/<int:pk>/<int:id>/', views.campaign_address_add, name='campaign_address_add'),
    path('address_select/<int:pk>/', views.campaign_address_select, name='campaign_address_select'),

]
