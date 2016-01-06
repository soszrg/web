from django.conf.urls import patterns, url
from BlogPost import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^home/$', views.home_page, name='blog_home'),
    url(r"^new_blog/$", views.new_blog, name = 'new_blog'),
    url(r'^new_blog/add_blog/$', views.add_blog),
    url(r'^detail/(?P<blog_id>\d+)/$', views.detail, name="detail"),
    url(r"^register/$", views.register),
    url(r'^register/add_user/$', views.add_user),
    url(r"^detail/(?P<blog_id>\d+)/tag/$", views.tag),
    url(r"^detail/(?P<blog_id>\d+)/tag/add_tag/$", views.add_tags),
    url(r'^$', views.login),
    url(r'^login_check/$', views.login_check),
    )

