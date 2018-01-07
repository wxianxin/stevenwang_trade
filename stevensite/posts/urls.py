from django.conf.urls import url                                                

from . import views

app_name = 'posts'
# namespacing URL names

urlpatterns = [ 
    url(r'^article/(?P<pk_name>[\S]+)/$', views.article_view, name='detail'),
    url(r'^static_html/(?P<file_name>[\S]+)/$', views.static_HTML, name='static_html'),
    url(r'^static_pdf/(?P<file_name>[\S]+)/$', views.static_pdf, name='static_pdf'),
]
