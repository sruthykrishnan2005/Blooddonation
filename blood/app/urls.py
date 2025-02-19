from django.urls import path
from .import views

urlpatterns = [ 
    path('',views.blood_login),

    #------------------admin----------------#
    path('admin_home',views.admin_home),
    path('logout/',views.blood_logout),
    path('add_blood_request', views.add_blood_request),
    path('edit_patient/<pid>',views.edit_patient),
    path('delete_patient/<pid>',views.delete_patient),
    path('view_register_donate/',views.view_register_donate),
   



    #------------------user-----------------#
    path('user_home', views.user_home),
    path('register/',views.Register),
    path('about_us', views.about_us),
    path('view_patient/<int:pid>/',views.view_patient),
    path('contact/', views.contact),
    path('register_to_donate/', views.register_to_donate),
    path('blood_donation_request', views.blood_donation_request),
]