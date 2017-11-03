from django.shortcuts import get_object_or_404, render                      
from django.urls import reverse
from django.views import generic

from .models import Article

class IndexView(generic.ListView):
    template_name = 'content_list/index.html'
    category = Article
    # context_object_name = 'article_list'

    def get_queryset(self):
        """get titles of every article"""
        return Article.objects.all()
    

    #def get_category(self):
    #    first_article = Article.objects.get(pk=1)
    #    category = first_article.category_text
    #    return category

