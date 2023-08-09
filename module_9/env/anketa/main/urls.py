from django.contrib import admin
from django.urls import path, include
from . import views
from .views import MyLoginView, MyLogoutView, profile, ProfileEditView, PasswordEditView, RegisterView, RegisterDoneView

urlpatterns = [
    path('', views.index, name="Главная страница"),
    path('accounts/login/', MyLoginView.as_view()),
    path('accounts/logout/', MyLogoutView.as_view(), name='logout'),
    path('accounts/password/edit/', PasswordEditView.as_view(), name='password_edit'),
    path('accounts/profile/edit/', ProfileEditView.as_view(), name='profile_edit'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', RegisterView.as_view(), name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
]
