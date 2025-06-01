from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Attendance, LeaveRequest, Alert

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'department')
    list_filter = ('role', 'department')
    fieldsets = (
        *UserAdmin.fieldsets,
        ('Additional Info', {'fields': ('role', 'department', 'phone')})
    )

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'status', 'check_in', 'check_out')
    list_filter = ('status', 'date')
    search_fields = ('user__username', 'user__email')

class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'start_date', 'end_date', 'leave_type', 'status', 'applied_on')
    list_filter = ('status', 'leave_type')
    search_fields = ('user__username', 'user__email')

class AlertAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('user__username', 'message')

admin.site.register(User, CustomUserAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(LeaveRequest, LeaveRequestAdmin)
admin.site.register(Alert, AlertAdmin)
