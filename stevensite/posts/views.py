from django.shortcuts import get_object_or_404, render                          
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Post

class ArticleView(generic.DetailView):
    template_name = 'posts/article.html'
