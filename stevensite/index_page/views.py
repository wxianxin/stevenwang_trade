from django.views import generic

from .models import Article, StockArticle

# Create your views here.
class HomePageView(generic.ListView):
    template_name = 'index_page/home.html'

    def get_queryset(self):
        return Article.objects.all()

#class HomePageView(generic.base.TemplateView):
#
#    template_name = 'index_page/home.html'
#
#    def get_article_list(self, **kwargs):
#        article_list= Article.objects.all()
#        return article_list

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

