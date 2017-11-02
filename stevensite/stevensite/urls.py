from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', include('index_page.urls')),
    url(r'^polls/', include('polls.urls')),
    url(r'^content_list/', include('content_list.urls')),
    url(r'^admin/', admin.site.urls),
]
