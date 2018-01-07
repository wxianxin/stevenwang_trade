from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('index_page.urls')),
    url(r'^posts/', include('posts.urls')),
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]
