from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clothes/', views.clothes_index, name='category'),
    path('clothes/create/', views.ClothesCreate.as_view(), name='clothes_create'),
    path('accounts/signup/', views.signup, name='signup'),
]