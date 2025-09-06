# accounts/urls.py
from django.urls import path
from .views import RegisterView, login_view # login_view'i import et

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', login_view, name='login'), # Yeni login path'ini ekle
]