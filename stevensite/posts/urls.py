from django.conf.urls import url                                                

from . import views

app_name = 'posts'
# url namespacing

urlpatterns = [ 
    url(r'^(?P<pk>[0-9]+)/$', views.ArticleView.as_view(), name='detail'),
]
