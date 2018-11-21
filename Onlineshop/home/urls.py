from django.urls import path
from . import  views


urlpatterns = [
    path('',views.index),
    path('home/', views.home, name='index'),
    path('login/', views.user_login, name='user_login'),
    path('success/', views.success, name='success'),
    path('checkout/', views.checkout, name='checkout'),
    path('cart/', views.cart, name='cart'),
    # path('logout/', views.user_logout, name='user_logout'),
]
