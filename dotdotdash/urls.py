from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
	url(r'^$', 'dotdotdash.views.home', name='home'),
	url(r'^sticky/', 'dotdotdash.views.sticky'),
    url(r'^projects/(?P<project>[\w|\W]+)/(?P<page>[\w|\W]+)/$', 'dotdotdash.views.projects'),
	# Examples:

    # url(r'^$', 'dotdotdash.views.home', name='home'),
    # url(r'^dotdotdash/', include('dotdotdash.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
)
