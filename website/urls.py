from django.conf.urls import patterns, include, url
from django.contrib import admin
from portofolio import views

urlpatterns = patterns('',
    # Examples:
     url(r'^$', views.HomeView.as_view(), name='index'),
    url(r'^portofolio/', include('portofolio.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
