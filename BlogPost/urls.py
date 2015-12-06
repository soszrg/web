from django.conf.urls import patterns, url
from BlogPost import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.home_page),
    url(r"^new_blog/$", views.new_blog),
    url(r'^new_blog/add_blog/$', views.add_blog),
    url(r'^detail/(?P<blog_id>\d+)/$', views.detail, name="detail"),
    url(r"^register/$", views.register),
    url(r'^register/add_user/', views.add_user),
    )

