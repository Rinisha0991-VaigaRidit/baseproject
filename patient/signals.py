from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from patient.models import Patient

@receiver(post_save, sender=User)
def create_patient_profile(sender, instance, created, **kwargs):
    if created:
        Patient.objects.create(user=instance)
