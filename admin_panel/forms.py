from django import forms
from django.contrib.auth.models import User
from .models import Facility

class FacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = ['name', 'location', 'phone_number']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class UserManagementForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_active', 'is_staff']

