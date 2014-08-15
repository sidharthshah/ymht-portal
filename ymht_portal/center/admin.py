from django.contrib import admin
from ymht.models import Coordinator, Center
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

    def queryset(self, request):
        qs = super(SessionAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs

        if not Coordinator.objects.filter(user=request.user).exists():
            return Session.objects.none()

        current_coordinator = Coordinator.objects.get(user=request.user)
        if not Center.objects.filter(coordinators__in=[current_coordinator]):
            return Session.objects.none()

        current_center = Center.objects.get(coordinators__in=[current_coordinator])

        #Return data for city link
        if request.user.groups.filter(name='City Link').exists():
        	current_city = current_center.city
        	city_centers = Center.objects.filter(city__in=[current_city])
        	return qs.filter(center__in=[center for center in city_centers])

        #Return data for co-ordiantors
        return qs.filter(center=current_center)

admin.site.register(Session, SessionAdmin)
