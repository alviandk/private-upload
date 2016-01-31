from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static # New Import

from portofolio import views

urlpatterns = [
   
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^accounts/', include('django.contrib.auth.urls', namespace="auth")),
    url(r'^$', views.HomeView.as_view(), name='index'),
    url(r'^portofolio/', include('portofolio.urls')),
    
    
]

if not settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

"""
urlpatterns = patterns('',
    # Examples:
     url(r'^$', views.HomeView.as_view(), name='index'),
    url(r'^portofolio/', include('portofolio.urls')),

    url(r'^reviews/', include('reviews.urls', namespace="reviews")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls', namespace="auth")),

    url(r'^api/token/', obtain_auth_token, name='api-token'),
    url(r'^api/', include(router.urls)),
)
"""
