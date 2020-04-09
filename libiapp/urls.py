from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^socios/$', views.SocioListView.as_view(), name='socios'),
    url(r'^socio/(?P<pk>\d+)$', views.SocioDetailView.as_view(), name='socio-detail'),
    url(r'^socio/create/$', views.SocioCreate.as_view(), name='socio_create'),
    url(r'^socio/(?P<pk>\d+)/update/$', views.SocioUpdate.as_view(), name='socio_update'),
    url(r'^socio/(?P<pk>\d+)/delete/$', views.SocioDelete.as_view(), name='socio_delete'),
]
