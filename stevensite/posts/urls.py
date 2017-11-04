from django.conf.urls import url                                                

from . import views

app_name = 'posts'

urlpatterns = [ 
    url(r'^(?P<pk>[a-z]+)/$', views.ArticleView.as_view(), name='detail'),
    url(r'^static_html/(?P<file_name>[^/s]+)/$', views.static_HTML, name='static_HTML'),
]
