from django.urls import path, include
from . import views
urlpatterns = [
    path('index', views.index, name="Index"),
    path('info', views.info, name="Info"),
]