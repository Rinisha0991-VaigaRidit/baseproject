from django.contrib import admin
from .models import Patient, Appointment, MedicalHistory, Billing, HealthEducationResource

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number', 'address',  'gender']

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient', 'doctor', 'date', 'time', 'status']
    list_filter = ['status', 'date']
    search_fields = ['patient__user__username', 'doctor__user__username']

@admin.register(MedicalHistory)
class MedicalHistoryAdmin(admin.ModelAdmin):
    list_display = ['patient', 'diagnosis', 'date']
    search_fields = ['patient__user__username', 'diagnosis']

@admin.register(Billing)
class BillingAdmin(admin.ModelAdmin):
    list_display = ['patient', 'appointment', 'amount', 'date', 'paid']
    list_filter = ['paid', 'date']

@admin.register(HealthEducationResource)
class HealthEducationResourceAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']
