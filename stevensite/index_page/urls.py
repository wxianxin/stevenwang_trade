from django.conf.urls import url

from . import views

app_name = 'index_page'

urlpatterns = [
    url(r'^$', views.HomepageView.as_view(), name='homepage'),
    url(r'^stocks/$', views.StocksView.as_view(), name='stocks'),
]
