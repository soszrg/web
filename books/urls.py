from django.conf.urls import url, patterns
from forms import AuthorForm,BookForm,PubForm
import views
from django.views.generic.base import TemplateView
from django.contrib.auth import views as authViews
urlpatterns = patterns('',
                       url(r'^$', views.home_page, name='home_page'),
#                        (r'^search-form/$', views.search_form),
                       url(r'^search/$', views.search),
                       url(r'^contract/$', views.contract),
                       url(r'^thanks/(?P<str>.+)$', views.thanks,name='thanks'),
                       url(r'^new_author/$', views.new_item, {'form':AuthorForm, 'type':'author'}, name='new_author'),
                       url(r'^new_pub/$', views.new_item, {'form':PubForm, 'type':'publisher'}, name='new_pub'),
                       url(r'^new_book/$', views.new_item, {'form':BookForm, 'type':'book'}, name='new_book'),
                       url(r'^about/$', TemplateView.as_view(template_name='about.html')),
                       url(r'^register/$', views.register, name = "register"),
#                         url(r'login/$', authViews.login, {'template_name':'login.html'}, name="auth_login"),
#                        url(r'logout/$', views.logout),
                    )
