from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework.authtoken.views import obtain_auth_token

from board.urls import router
from portofolio import views

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
