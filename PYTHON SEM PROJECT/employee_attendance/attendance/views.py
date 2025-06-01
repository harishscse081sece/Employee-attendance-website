from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from datetime import datetime
import pytz

def get_ist_time():
    ist = pytz.timezone('Asia/Kolkata')
    return timezone.now().astimezone(ist)

from .models import User, Attendance, LeaveRequest, Alert
from .forms import UserRegistrationForm, LeaveRequestForm
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.is_authenticated and user.role == 'admin'

def is_manager(user):
    return user.is_authenticated and user.role == 'manager'

@login_required
def dashboard(request):
    user = request.user
    today = get_ist_time().date()
    try:
        attendance = Attendance.objects.get(user=user, date=today)
    except Attendance.DoesNotExist:
        attendance = None
    
    context = {
        'attendance': attendance,
        'alerts': Alert.objects.filter(user=user, is_read=False),
        'leave_requests': LeaveRequest.objects.filter(user=user).order_by('-applied_on')[:5]
    }
    
    if user.role in ['admin', 'manager']:
        context['pending_leaves'] = LeaveRequest.objects.filter(status='pending')
    
    return render(request, 'attendance/dashboard.html', context)

@login_required
def mark_attendance(request):
    user = request.user
    today = get_ist_time().date()
    current_time = get_ist_time()
    
    attendance, created = Attendance.objects.get_or_create(
        user=user,
        date=today,
        defaults={'status': 'present'}
    )
    
    if not attendance.check_in:
        attendance.check_in = current_time
        attendance.save()
        messages.success(request, 'Check-in recorded successfully!')
    elif not attendance.check_out:
        attendance.check_out = current_time
        attendance.save()
        messages.success(request, 'Check-out recorded successfully!')
    else:
        messages.warning(request, 'You have already completed your attendance for today!')
    
    return redirect('dashboard')

@login_required
def leave_request(request):
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.user = request.user
            leave.save()
            messages.success(request, 'Leave request submitted successfully!')
            return redirect('dashboard')
    else:
        form = LeaveRequestForm()
    
    return render(request, 'attendance/leave_request.html', {'form': form})

@user_passes_test(is_manager)
def manage_leave_requests(request):
    if request.method == 'POST':
        leave_id = request.POST.get('leave_id')
        action = request.POST.get('action')
        
        try:
            leave = LeaveRequest.objects.get(id=leave_id)
            leave.status = action
            leave.reviewed_by = request.user
            leave.review_date = timezone.now()
            leave.save()
            
            Alert.objects.create(
                user=leave.user,
                message=f'Your leave request from {leave.start_date} to {leave.end_date} has been {action}.'
            )
            
            messages.success(request, f'Leave request {action} successfully!')
        except LeaveRequest.DoesNotExist:
            messages.error(request, 'Leave request not found!')
    
    pending_requests = LeaveRequest.objects.filter(status='pending')
    return render(request, 'attendance/manage_leaves.html', {'leaves': pending_requests})

@user_passes_test(is_admin)
def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User registered successfully!')
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'attendance/register_user.html', {'form': form})

@login_required
def view_attendance_history(request):
    user = request.user
    attendance_history = Attendance.objects.filter(user=user).order_by('-date')
    return render(request, 'attendance/attendance_history.html', {'history': attendance_history})
