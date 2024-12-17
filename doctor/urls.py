from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'doctor'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('', views.doctor_dashboard, name='doctor_dashboard'),
    path('create_or_edit_profile/', views.create_or_edit_profile, name='create_or_edit_profile'),

    path('schedule_appointment/', views.schedule_appointment, name='schedule_appointment'),
    path('prescribe_medication/<int:appointment_id>/', views.prescribe_medication, name='prescribe_medication'),




]

