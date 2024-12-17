from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Doctor

@receiver(post_save, sender=User)
def create_doctor_profile(sender, instance, created, **kwargs):
    if created:
        # Automatically create a Doctor object for every new user
        Doctor.objects.create(user=instance)
