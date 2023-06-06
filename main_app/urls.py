from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('clothes/', views.clothes_index, name='index'),
    path('clothes/create/', views.ClothesCreate.as_view(), name='clothes_create')
]