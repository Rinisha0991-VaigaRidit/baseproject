from django.db import models
from django.contrib.auth.models import User

class Facility(models.Model):
    name = models.CharField(max_length=100)

    location = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)


class UserManagement(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=[('Doctor', 'Doctor'), ('Admin', 'Admin'), ('Patient', 'Patient')])
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE, null=True, blank=True, default=None)



