from django.contrib import admin
from ymht.models import *
from .models import Session, SessionMedia, Attendance
from django.core.exceptions import ValidationError

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
