from django.conf.urls import url

from . import views

app_name = 'index_page'

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home_page'),
    #url(r'^aricles/', views.AritcleView.as_view(), name='article'),

    url(r'^stocks/$', views.StocksView.as_view(), name='stocks'),
]
