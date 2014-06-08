from django.contrib import admin
from .models import YMHT, Coordinator, YMHTMobile, YMHTEmail

class YMHTMobileInline(admin.TabularInline):
    model = YMHTMobile

class YMHTEmailInline(admin.TabularInline):
    model = YMHTEmail

class YMHTAdmin(admin.ModelAdmin):
    inlines = [
        YMHTMobileInline,
        YMHTEmailInline
    ]

admin.site.register(YMHT, YMHTAdmin)
admin.site.register(Coordinator)
