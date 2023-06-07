from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('clothing/', views.clothes_index, name='index'),
    path('clothing/tops', views.tops_index, name='tops_index'),
    path('clothing/bottoms', views.bottoms_index, name='bottoms_index'),
    path('clothing/jackets', views.jackets_index, name='jackets_index'),
    path('clothing/dresses', views.dresses_index, name='dresses_index'),
    path('clothing/jumpsuits', views.jumpsuits_index, name='jumpsuits_index'),
    path('clothing/shoes', views.shoes_index, name='shoes_index'),
    path('clothing/accessories', views.accessories_index, name='accessories_index'),
    path('clothing/<int:clothes_id>/', views.clothes_detail, name='detail'),
    path('clothing/create/', views.ClothesCreate.as_view(), name='clothing_create'),
    path('clothing/<int:pk>/update/', views.ClothesUpdate.as_view(), name='clothing_update'),
    path('clothing/<int:pk>/delete/', views.ClothesDelete.as_view(), name='clothing_delete'),
    path('clothing/bag', views.bag, name='bag'),
    path('clothing/likes', views.likes, name='likes'),
    path('clothing/<int:clothes_id>/add_photo/', views.add_photo, name='add_photo')
]

