from django.contrib import admin
from .models import (YMHT, Coordinator, YMHTMobile, Hobby,
                    YMHTEmail, YMHTAddress, YMHTEducation, YMHTJob, City,
                    State, Country, Center, Membership,
                    Event, SevaDetails)

from center.models import *

class YMHTMobileInline(admin.TabularInline):
    model = YMHTMobile

class YMHTEmailInline(admin.TabularInline):
    model = YMHTEmail

class YMHTAddressInline(admin.TabularInline):
    model = YMHTAddress

class YMHTEducationInline(admin.TabularInline):
    model = YMHTEducation

class YMHTJobInline(admin.TabularInline):
    model = YMHTJob

class YMHTMembershipInline(admin.TabularInline):
    fields = ('ymht' , 'center' , 'coordinator', 'age_group' , 'role', 'since', 'till')
    model = Membership

class YMHTSevaDetailsInline(admin.TabularInline):
    fields = ('event', 'ymht' , 'coordinator', 'attended' , 'attended_days' , 'comments')
    model = SevaDetails


class YMHTAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'gnan_date')
    inlines = [
        YMHTMobileInline,
        YMHTEmailInline,
        YMHTAddressInline,
        YMHTEducationInline,
        YMHTJobInline,
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
admin.site.register(Hobby)
admin.site.register(YMHT, YMHTAdmin)
admin.site.register(Coordinator)
admin.site.register(Membership)

