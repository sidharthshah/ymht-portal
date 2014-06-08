from django.contrib import admin
from .models import (YMHT, Coordinator, YMHTMobile,
                    YMHTEmail, YMHTAddress, City,
                    State, Country, Center, Membership)

class YMHTMobileInline(admin.TabularInline):
    model = YMHTMobile

class YMHTEmailInline(admin.TabularInline):
    model = YMHTEmail

class YMHTAddressInline(admin.TabularInline):
    model = YMHTAddress

class YMHTMembershipInline(admin.TabularInline):
    fields = ('ymht' , 'center' , 'age_group' , 'role', 'since', 'till')
    model = Membership

class YMHTAdmin(admin.ModelAdmin):
    inlines = [
        YMHTMobileInline,
        YMHTEmailInline,
        YMHTAddressInline,
        YMHTMembershipInline
    ]

admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)

admin.site.register(Center)
admin.site.register(YMHT, YMHTAdmin)
admin.site.register(Coordinator)
