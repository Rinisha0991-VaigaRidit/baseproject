from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'patient'

urlpatterns = [
    path(' ', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('patient_dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('book_appointment/', views.book_appointment, name='book_appointment'),
    path('medical_history/', views.medical_history, name='medical_history'),
    path('billing_payments/', views.billing_payments, name='billing_payments'),
    path('health_resources/', views.health_resources, name='health_resources'),
]
