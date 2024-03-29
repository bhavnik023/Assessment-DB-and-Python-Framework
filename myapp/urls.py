from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('service/',views.service,name='service'),
    path('cotact/',views.contact,name='contact'),
    path('appointment/',views.appointment,name='appointment'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('forgot-password/',views.forgot_password,name='forgot-password'),
    path('logout/',views.logout,name='logout'),
    path('verify-otp/',views.verify_otp,name='verify-otp'),
    path('new-password/',views.new_password,name='new-password'),
    path('change-password/',views.change_password,name='change-password'),
    path('doctor-view-appointment/',views.doctor_view_appointment,name='doctor-view-appointment'),
    path('view-doctor/',views.view_doctor,name='view-doctor'),
    path('profile/',views.profile,name='profile'),
]