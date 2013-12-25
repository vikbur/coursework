from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^question/', include('question.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^inquirer/', include('inquirer.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
