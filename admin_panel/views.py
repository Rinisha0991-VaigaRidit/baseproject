from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.models import User
from django.contrib import messages
from patient.models import Appointment
from .models import Facility
from .forms import FacilityForm, UserManagementForm

# Admin dashboard

def admin_dashboard(request):
    total_users = User.objects.count()
    total_facilities = Facility.objects.count()
    total_appointments = Appointment.objects.count()
    context = {
        'total_users': total_users,
        'total_facilities': total_facilities,
        'total_appointments': total_appointments,
    }
    return render(request, 'admin_panel/admin_dashboard.html', context)

# Add Facility

def add_facility(request):
    if request.method == 'POST':
        form = FacilityForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Facility added successfully!')
            return redirect('admin_panel:add_facility')
    else:
        form = FacilityForm()
    facilities = Facility.objects.all()
    return render(request, 'admin_panel/add_facility.html', {'form': form, 'facilities': facilities})

# Manage Users

def manage_users(request):
    users = User.objects.all()
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        action = request.POST.get('action')
        user = get_object_or_404(User, id=user_id)
        if action == 'activate':
            user.is_active = True
            user.save()
            messages.success(request, f'User {user.username} activated.')
        elif action == 'deactivate':
            user.is_active = False
            user.save()
            messages.success(request, f'User {user.username} deactivated.')
        return redirect('admin_panel:manage_users')
    return render(request, 'admin_panel/manage_users.html', {'users': users})

# Manage Appointments

def manage_appointments(request):
    appointments = Appointment.objects.all()
    context = {
        'appointments': appointments,
    }
    return render(request, 'admin_panel/manage_appointments.html', context)
