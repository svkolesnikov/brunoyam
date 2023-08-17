from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="campaign"),
    path('add/', views.campaign_add, name='campaign_add'),
    path('view/<int:pk>/', views.campaign_view, name='campaign_view'),
    path('stat/<int:pk>/', views.campaign_stat, name='campaign_stat'),
    path('edit/<int:pk>/', views.campaign_edit, name='campaign_edit'),
    path('del/<int:pk>/', views.campaign_del, name='campaign_del'),
    path('address_add/<int:pk>/<int:id>/', views.campaign_address_add, name='campaign_address_add'),
    path('address_del/<int:pk>/<int:id>/', views.campaign_address_delete, name='campaign_address_del'),
    path('address_select/<int:pk>/', views.campaign_address_select, name='campaign_address_select'),
    path('user_select/<int:pk>/', views.campaign_user_select, name='campaign_user_select'),
    path('user_add/<int:pk>/<int:id>/', views.campaign_user_add, name='campaign_user_add'),
    path('user_del/<int:pk>/<int:id>/', views.campaign_user_delete, name='campaign_user_del'),
    path('survey_add/<int:pk>/<int:id>/', views.survey_add, name='survey_add'),
    path('address_state/<int:pk>/<int:id>/', views.address_state, name='address_state'),

]
