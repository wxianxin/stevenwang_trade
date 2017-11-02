from django.views.generic.base import TemplateView

from content_list.models import Article

class HomePageView(TemplateView):

    template_name = 'index_page/index.html'

    def get_article_list(self, **kwargs):
        article_list= Article.objects.all()[:5]
        return article_list

# Create your views here.
