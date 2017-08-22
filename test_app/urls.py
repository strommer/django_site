from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='Login'),
    url(r'^process/$', views.login_process, name='Process')
]