from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='admin/')),
    url(r'^admin/', include(admin.site.urls)),
    
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

