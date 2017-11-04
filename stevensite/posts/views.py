from django.shortcuts import get_object_or_404, render                          
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Post

class ArticleView(generic.DetailView):
    model = Post
    #template_name = 'posts/article.html'

def static_HTML(request, file_name):
    file_path = 'posts/' + file_name + '.html'
    return render(request, file_path)

