from django.urls import path
from .import views

urlpatterns = [ 
    path('',views.login),

    #------------------admin----------------#
    path('shop_home',views.admin_home),

    #------------------user-----------------#
    path('register',views.register),
    path('user_home',views.user_home),
  
]