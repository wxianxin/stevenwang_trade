from django.views import generic

from .models import Article, LinkToPostStatic, StockArticle

# Create your views here.
class HomepageView(generic.ListView):
    template_name = 'index_page/home.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(generic.ListView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the models 
        context['article_link_list'] = LinkToPostStatic.objects.all()
        context['quick_link_list'] = LinkToPostStatic.objects.all()
        return context


    def get_queryset(self):
        return LinkToPostStatic.objects.all()

class IndexView(generic.ListView):
    template_name = 'index_page/list.html'


class StocksView(generic.ListView):

    template_name = 'index_page/stocks.html'
    #category = stock_article_list[0].category_text 
    context_object_name = 'stock_article_list'

    def get_queryset(self):
        stock_article_list = StockArticle.objects.all()
        return stock_article_list
    

    #def get_category(self):
    #    first_article = Article.objects.get(pk=1)
    #    category = first_article.category_text
    #    return category

