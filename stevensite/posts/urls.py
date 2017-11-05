from django.conf.urls import url                                                

from . import views

app_name = 'posts'

urlpatterns = [ 
    url(r'^(?P<pk>[a-z]+)/$', views.ArticleView.as_view(), name='detail'),
    url(r'^static_html/(?P<file_name>[^/s]+)/$', views.static_HTML, name='static_html'),
    #url(r'^static_html/quick_link/(?P<file_name>[^/s]+)/$', views.static_HTML, name='quick_link_static_html'),
    url(r'^static_pdf/(?P<file_name>[^/s]+)/$', views.static_pdf, name='static_pdf'),
]
