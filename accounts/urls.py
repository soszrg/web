#encoding = utf8

from django.conf.urls import url, patterns
from django.contrib.auth import views as authViews

urlpatterns = patterns('',
                       url(r'^login/', authViews.login, {'template_name':'login.html'}, name="auth_login"),
                       url(r'^logout/', authViews.logout, {'template_name':'logout.html'}, name="auth_logout"),
                       )