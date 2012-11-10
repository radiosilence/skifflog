from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'skifflog.views.home', name='home'),
    url(r'^dashboard/$', 'skifflog.views.dashboard', name='dashboard'),
    url(r'^arrive/$', 'skifflog.views.arrive', name='arrive'),
    url(r'^depart/$', 'skifflog.views.depart', name='depart'),
    url(r'^check/$', 'skifflog.views.check', name='check'),
    url(r'^accounts/profile/$', 'skifflog.views.profile', name='account_profile'),
    (r'^accounts/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
