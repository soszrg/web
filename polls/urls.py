#conding = utf-8

from django.conf.urls import patterns, url

from polls import views
from django.conf.urls.i18n import urlpatterns

urlpatterns=patterns('',
                     url(r'^$', views.index, name='index'),
                     url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
                     url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
                     url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
                    )