from builtins import hasattr, getattr, print, ValueError
from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .decorators import doctor_required
from django.contrib import messages
from doctor.models import Doctor
from .forms import DoctorProfileForm
from .models import Doctor, AppointmentSchedule, Prescription
from patient.models import Appointment, Patient
from .forms import AppointmentScheduleForm, PrescriptionForm
from django.contrib.auth.models import User
from patient.forms import AppointmentForm
# Doctor Dashboard


@doctor_required
@login_required
def doctor_dashboard(request):
    if not hasattr(request.user, 'doctor_profile'):
        return redirect('doctor:create_or_edit_profile')
    doctor = request.user.doctor_profile
    appointments = Appointment.objects.filter(doctor=doctor, status='Scheduled').order_by('date', 'time')
    return render(request, 'doctor/doctor_dashboard.html', {'doctor': doctor, 'appointments': appointments})


# Create or Edit Doctor Profile
@login_required
def create_or_edit_profile(request):
    doctor = getattr(request.user, 'doctor_profile', None)  # Retrieve doctor profile if it exists

    if request.method == 'POST':
        form = DoctorProfileForm(request.POST, instance=doctor)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('doctor:doctor_dashboard')  # Redirect to the dashboard or any relevant page
    else:
        form = DoctorProfileForm(instance=doctor)

    return render(request, 'doctor/create_or_edit_profile.html', {'form': form, 'doctor_profile': doctor})


# Manage Appointment Schedule



@login_required
def schedule_appointment(request):
    doctor = Doctor.objects.filter(user=request.user).first()

    # If no Patient record is found
    if not doctor:
        # Redirect the user to a registration page or show a message
        error_message = "You must create a doctor profile before scheduling appointment."
        return render(request, 'doctor/schedule_appointment.html', {'error_message': error_message})
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.doctor = doctor
            schedule.save()
            messages.success(request, 'Appointment scheduled successfully!')
            return redirect('doctor:schedule_appointment')
    else:
        form = AppointmentForm()
    schedules = Appointment.objects.filter(doctor=doctor).order_by('date', 'time')

    return render(request, 'doctor/schedule_appointment.html', {'form': form, 'schedules': schedules})

# Prescribe Medication
@login_required
def prescribe_medication(request, appointment_id):
    
    doctor = Doctor.objects.filter(user=request.user).first()

    # If no Patient record is found
    if not doctor:
        # Redirect the user to a registration page or show a message
        error_message = "You must create a doctor profile before prescribing medication."
        return render(request, 'doctor/prescribe_medication.html', {'error_message': error_message})
    appointment = get_object_or_404(Appointment, id=appointment_id, doctor=doctor)
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            prescription = form.save(commit=False)
            prescription.appointment = appointment
            prescription.doctor = doctor
            prescription.patient = appointment.patient
            prescription.save()
            messages.success(request, 'Prescription created successfully!')
            return redirect('doctor:doctor_dashboard')
    else:
        form = PrescriptionForm()

    context = {'form': form, 'appointment': appointment}
    return render(request, 'doctor/prescribe_medication.html', context)

