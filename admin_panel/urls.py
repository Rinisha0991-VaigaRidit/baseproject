from django.urls import path
from . import views

app_name = 'admin_panel'

urlpatterns = [
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('add_facility/', views.add_facility, name='add_facility'),
    path('manage_users/', views.manage_users, name='manage_users'),
    path('manage_appointments/', views.manage_appointments, name='manage_appointments'),
]
