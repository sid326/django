from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'minipro.views.home', name='home'),
    url(r'^project/', include('project.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
)
