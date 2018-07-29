from django.views import generic

from .models import *
from posts.models import Article

# Create your views here.
class HomepageView(generic.ListView):
    template_name = 'index_page/home.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(generic.ListView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the models 
        context['article_list'] = Article.objects.order_by('-pub_date')
        context['article_link_list'] = LinkToPostStatic.objects.filter(name_text__startswith="article_")
        context['article_pdf_list'] = PdfFile.objects.filter(name_text__startswith="article_")
        context['reading_pdf_list'] = PdfFile.objects.filter(name_text__startswith="reading_")
        context['notes_list'] = LinkToPostStatic.objects.filter(name_text__startswith='note_')
        context['notes_pdf_list'] = PdfFile.objects.filter(name_text__startswith="note_")
        context['toolbox_pdf_list'] = PdfFile.objects.filter(name_text__startswith="toolbox_")
        return context


    # How to remove this duplication?
    def get_queryset(self):
        return LinkToPostStatic.objects.all()

class IndexView(generic.ListView):
    template_name = 'index_page/list.html'


class StocksView(generic.ListView):

    template_name = 'index_page/stocks.html'
    context_object_name = 'stock_article_list'

    def get_queryset(self):
        stock_article_list = LinkToPostStatic.objects.filter(name_text__startswith="stock_")
        return stock_article_list
    

    #def get_category(self):
    #    first_article = Article.objects.get(pk=1)
    #    category = first_article.category_text
    #    return category

