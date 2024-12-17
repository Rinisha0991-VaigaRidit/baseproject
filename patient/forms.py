from django import forms
from django.contrib.auth.models import User
from .models import Patient, Appointment

class PatientRegistrationForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=15)
    address = forms.CharField(widget=forms.Textarea)

    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        exclude = ['patient']
        fields = ['doctor', 'date', 'time', 'status']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }
