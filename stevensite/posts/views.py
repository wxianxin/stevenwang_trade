from django.shortcuts import get_object_or_404, render                          
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Article

# class ArticleView(generic.TemplateView):
#     #model = Article #???? what is this for? (name_for_admin?) 
#     template_name = 'posts/article_template.html'
#     context_object_name = 'article'
# 
#     def get_context_data(self, **kwargs):
#         context = super(generic.TemplateView, self).get_context_data(**kwargs)
#         context['name'] = Article.objects.filter(name_text__exact = 'test')
#         return context

def article_view(request, pk_name):
    model = Article #???? what is this for? (name_for_admin?) 
    template_name = 'posts/article_template.html'
    article = get_object_or_404(Article, pk=pk_name)
    context = {'article': article,}

    return render(request, template_name, context)

def static_HTML(request, file_name):
    file_path = 'posts/' + file_name + '.html'
    return render(request, file_path)

def static_pdf(request, file_name):
    url = 'http://stevenwang.trade/static/posts/pdf/' + file_name + '.pdf'
    return HttpResponseRedirect(url)

#def static_pdf(request, file_name):
#    file_path = 'posts/static/posts/pdf/' + file_name + '.pdf'
#
#    with open(file_path, 'rb') as pdf:
#        response = HttpResponse(pdf.read(), content_type='application/pdf')
#        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
#        return response
#    pdf.closed
