

from django.db import models
from django.contrib.auth.models import User



class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_profile')
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])


    def __str__(self):
        return self.user.username


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey('doctor.Doctor', on_delete=models.CASCADE, related_name='appointments')
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField()

    STATUS_CHOICES = [
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Scheduled')

    def __str__(self):
        return f"Appointment with Dr. {self.doctor.user.username} on {self.date}"





class MedicalHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medical_history', null=True, blank=True, default=None)
    diagnosis = models.TextField()
    treatment = models.TextField()
    date = models.DateField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Medical History for {self.patient.user.username}"


class Billing(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='billing_records')
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE,  related_name='billing_records')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Billing Record for {self.patient.user.username}"


class HealthEducationResource(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)  # Make sure this is populated with valid URLs
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

