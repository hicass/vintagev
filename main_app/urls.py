from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('clothes/', views.clothes_index, name='index'),
    path('clothes/<int:pk>/update/', views.ClothingUpdate.as_view(), name='clothes_update'),
    path('clothes/<int:pk>/delete/', views.ClothingDelete.as_view(), name='clothes_delete'),
    path('clothes/bag', views.bag, name='bag'),
    path('clothes/likes', views.likes, name='likes'),
]