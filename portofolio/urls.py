from django.conf.urls import patterns, url
from portofolio import views

urlpatterns = patterns('',


    
    url(r'^cv-download/$', views.CVDownload.as_view(), name='cv-download'),
)
