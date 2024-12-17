from builtins import hasattr

from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from .models import Doctor

def doctor_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        # Check if the logged-in user has a doctor profile
        if hasattr(request.user, 'doctor_profile'):
            return view_func(request, *args, **kwargs)
        else:
            # Redirect to a page or display an error
            return redirect('doctor:create_or_edit_profile')  # Replace with the appropriate route
    return _wrapped_view
