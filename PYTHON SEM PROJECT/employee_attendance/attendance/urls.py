from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='attendance/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('mark-attendance/', views.mark_attendance, name='mark_attendance'),
    path('leave-request/', views.leave_request, name='leave_request'),
    path('manage-leaves/', views.manage_leave_requests, name='manage_leaves'),
    path('register-user/', views.register_user, name='register_user'),
    path('attendance-history/', views.view_attendance_history, name='attendance_history'),
]
