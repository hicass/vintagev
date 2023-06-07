from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('clothing/', views.clothes_index, name='index'),
    path('clothing/create/', views.ClothesCreate.as_view(), name='clothing_create'),
    path('clothing/<int:pk>/update/', views.ClothesUpdate.as_view(), name='clothing_update'),
    path('clothing/<int:pk>/delete/', views.ClothesDelete.as_view(), name='clothing_delete'),
    path('clothing/bag', views.bag, name='bag'),
    path('clothing/likes', views.likes, name='likes'),
]

