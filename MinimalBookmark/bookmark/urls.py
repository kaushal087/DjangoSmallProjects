from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.showHome, name='index'),
    url(r'^bookmark/(?P<url_id>[0-9]+)/$', views.showDetails, name='show'),
    url(r'^tags/(?P<tag_id>[0-9]+)/$', views.showTag, name='showTag'),
    url(r'^tags/$', views.showTags, name='showTags'),
    url(r'^tags/new/$', views.addTag, name='addTag'),
    url(r'^tags/new/insertTagAndShow/$', views.insertTagAndShow, name='InsertTagAndShow'),
    url(r'^tags/(?P<tag_id>[0-9]+)/edit$', views.editTag, name='editTag'),
    url(r'^tags/updateTagAndShow/(?P<tag_id>[0-9]+)/$', views.updateTagAndShow, name='updateTag'),
    url(r'^bookmark/(?P<url_id>[0-9]+)/edit$', views.editURL, name='editURL'),
    url(r'^bookmark/updateBookmarkAndShow/(?P<url_id>[0-9]+)/$', views.updateBookmarkAndShow, name='updateBookmarkAndShow'),

]

