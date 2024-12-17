from builtins import print

from django.shortcuts import render, redirect, get_object_or_404
from patient.models import Patient
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Patient, Appointment, MedicalHistory, Billing, HealthEducationResource
from .forms import PatientRegistrationForm, AppointmentForm
from django.utils.timezone import now
from django.http import Http404

# Patient Registration
def register(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if not Patient.objects.filter(user=user).exists():
                Patient.objects.create(user=user, phone_number=form.cleaned_data['phone_number'],
                                        address=form.cleaned_data['address'],

                                        gender=form.cleaned_data['gender'])

            messages.success(request, 'Registration successful! Please log in.')
            return redirect('patient:patient_dashboard')
    else:
        form = PatientRegistrationForm()
    return render(request, 'patient/register.html', {'form': form})


# Patient Dashboard

def patient_dashboard(request):
    # Attempt to fetch the Patient record
    patient = Patient.objects.filter(user=request.user).first()

    # If no Patient record is found
    if not patient:
        # Redirect the user to a registration page or show a message
        error_message = "You must create a patient profile before booking an appointment."
        return render(request, 'patient/patient_dashboard.html', {'error_message': error_message})
    appointments = Appointment.objects.filter(patient=patient)
    billing_records = Billing.objects.filter(patient=patient)
    context = {
        'patient': patient,
        'appointments': appointments,
        'billing_records': billing_records,
    }
    return render(request, 'patient/patient_dashboard.html', context)


# Appointment Booking

def book_appointment(request):
    patient = Patient.objects.filter(user=request.user).first()

    if not patient:
        error_message = "You must create a patient profile before booking an appointment."
        return render(request, 'patient/book_appointment.html', {'error_message': error_message})
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = patient
            appointment.save()
            messages.success(request, 'Appointment booked successfully!')
            return redirect('patient:patient_dashboard')
        else:
            # If the form is not valid, show errors
            messages.error(request, 'Please correct the errors below.')
    else:
        form = AppointmentForm()
    return render(request, 'patient/book_appointment.html', {'form': form})


# View Medical History

def medical_history(request):
    patient = Patient.objects.filter(user=request.user).first()
    if not patient:
        # Redirect to a registration page or show an appropriate error message
        error_message = "You must create a patient profile before viewing your patient medical history."
        return render(request, 'patient/medical_history.html', {'error_message': error_message})
    medical_history = MedicalHistory.objects.filter(patient=patient)
    return render(request, 'patient/medical_history.html', {'medical_history': medical_history})


# View Billing Records

def billing_payments(request):
    patient = Patient.objects.filter(user=request.user).first()
    if not patient:
        # Redirect to a registration page or show an appropriate error message
        error_message = "You must create a patient profile before viewing your bill."
        return render(request, 'patient/billing_payments.html', {'error_message': error_message})

    # Fetch billing records for the patient
    billing_records = Billing.objects.filter(patient=patient)
    print(billing_records)

    # Render the billing payments page
    return render(request, 'patient/billing_payments.html', {'billing_records': billing_records})





# Health Education Resources
def health_resources(request):
    resources = HealthEducationResource.objects.all()
    return render(request, 'patient/health_resources.html', {'resources': resources})

