from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.Login, name='Login'),
    url(r'^process/$', views.LoginProcess, name='Process')
]