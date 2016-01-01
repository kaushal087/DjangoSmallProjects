from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.showHome, name='index'),
    url(r'^bookmark/(?P<url_id>[0-9]+)/$', views.showDetails, name='show'),
]

