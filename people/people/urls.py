from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'people.views.home', name='home'),
    url(r'^sheet/(?P<ruleset_id>\d+)/(?P<character_id>\d+)/(?P<character_name>\w+)', 'general.views.char_sheet'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^create', 'general.views.create'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
