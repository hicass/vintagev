from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clothes/', views.clothes_index, name='category'),
    path('accounts/signup/', views.signup, name='signup'),
]