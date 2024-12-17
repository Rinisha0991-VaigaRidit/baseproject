from django.db import models
from django.contrib.auth.models import User


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')
    specialization = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    bio = models.TextField(blank=True, null=True)


    def __str__(self):
        return f"Dr. {self.user.username}"


class AppointmentSchedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='schedules', null=True, blank=True, default=None)
    day_of_week = models.CharField(max_length=20, choices=[
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ])
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.doctor.user.username} - {self.day_of_week}"


class Prescription(models.Model):
    appointment = models.OneToOneField('patient.Appointment', on_delete=models.CASCADE, related_name='prescription')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='prescriptions', null=True, blank=True, default=None)
    patient = models.ForeignKey('patient.Patient', on_delete=models.CASCADE, related_name='prescriptions', null=True, blank=True, default=None)
    medication = models.TextField()
    instructions = models.TextField()


    def __str__(self):
        return f"Prescription for {self.patient.user.username} by Dr. {self.doctor.user.username}"
