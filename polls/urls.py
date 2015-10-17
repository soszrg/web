#conding = utf-8

from django.conf.urls import patterns, url

from polls import views
from django.conf.urls.i18n import urlpatterns

urlpatterns=patterns('',
                     url(r'^$', views.index, name='index'),
                     url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
                    
                    )