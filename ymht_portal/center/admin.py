from django.contrib import admin
from .models import Session, SessionMedia, Attendance

class SessionMediaInline(admin.TabularInline):
    model = SessionMedia

class AttendanceInline(admin.TabularInline):
    model = Attendance

class SessionAdmin(admin.ModelAdmin):
    inlines = [
        SessionMediaInline,
        AttendanceInline
        ]

admin.site.register(Session, SessionAdmin)
