from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Article)
admin.site.register(LinkToPostStatic)
admin.site.register(QuickLink)
admin.site.register(StockArticle)

