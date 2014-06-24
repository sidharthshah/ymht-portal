from django.contrib import admin
from .models import (YMHT, Coordinator, YMHTMobile,
                    YMHTEmail, YMHTAddress, City,
                    State, Country, Center, Membership,
                    Event, SevaDetails)

from center.models import *

class YMHTMobileInline(admin.TabularInline):
    model = YMHTMobile

class YMHTEmailInline(admin.TabularInline):
    model = YMHTEmail

class YMHTAddressInline(admin.TabularInline):
    model = YMHTAddress

class YMHTMembershipInline(admin.TabularInline):
    fields = ('ymht' , 'center' , 'coordinator', 'age_group' , 'role', 'since', 'till')
    model = Membership

class YMHTSevaDetailsInline(admin.TabularInline):
    fields = ('event', 'ymht' , 'attended' , 'attended_days' , 'comments')
    model = SevaDetails

class YMHTAdmin(admin.ModelAdmin):
    exclude = ('user',)
    list_display = ('first_name', 'last_name', 'date_of_birth', 'gnan_date')
    inlines = [
        YMHTMobileInline,
        YMHTEmailInline,
        YMHTAddressInline,
        YMHTMembershipInline,
        YMHTSevaDetailsInline
    ]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user 
            obj.save()
            
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Event)
admin.site.register(Center)
admin.site.register(YMHT, YMHTAdmin)
admin.site.register(Coordinator)
admin.site.register(Membership)
admin.site.register(Attendance)

