from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sub/$', views.subrango, name='subrango'),
    #url(r'^about$', views.about, name='about'),
]