from django.conf.urls import url
from valeraBlog.apps.valeraBlogApp import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<slug>[\w\-]+)/$', views.getpost, name='getpost'),
]
