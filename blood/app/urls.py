from django.urls import path
from .import views

urlpatterns = [ 
    path('',views.blood_login),

    #------------------admin----------------#
    path('admin_home',views.admin_home,name='admin_home'),
    path('logout/',views.blood_logout),
    path('add_blood_request', views.add_blood_request),
    path('edit_patient/<pid>',views.edit_patient),
    path('delete_patient/<pid>',views.delete_patient),
    path('view_register_donate/',views.view_register_donate),
    path('view_request_blood',views.view_request_blood),



    #------------------user-----------------#
    path('user/home/', views.user_home, name='user_home'),
    path('user/logout/',views.blood_logout),
    path('register/', views.Register, name='register'),
    path('user/about_us/',views.about_us,name='about_us'),
    path('user/contact/', views.contact, name='contact'),   
    path('user/home/view_patient/<int:pid>/', views.view_patient, name='view_patient'),
    path('contact/', views.contact),
    path('user/register_to_donate/', views.register_to_donate),
    path('user/home/blood_donation_request', views.blood_donation_request, name='blood_donation_request'),
    path('user/view_request_blood_user/',views.view_request_blood_user),
    path('user/qty_in/<int:pk>/', views.qty_in, name='qty_in'),
    path('verify_otp/', views.verify_otp, name='verify_otp'),

]