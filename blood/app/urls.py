from django.urls import path
from .import views

urlpatterns = [ 
    path('',views.blood_login),

    #------------------admin----------------#
    path('admin_home',views.admin_home),
    path('logout',views.blood_logout),
    path('add_blood_request/', views.add_blood_request),

    #------------------user-----------------#
    path('user_home',views.user_home),
    path('register',views.Register),
    path('about_us', views.about_us),
]