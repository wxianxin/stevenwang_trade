from django.db import models

class Article(models.Model):
    category_text = models.CharField(max_length=50, default='category')
    title_text = models.CharField(max_length=200, default='title')
    name_text = models.CharField(max_length=20, default='name')
    subtitle_text = models.CharField(max_length=200, default='subtitle')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title_text


class StockArticle(Article):
    symbol_text = models.CharField(max_length=8)

    def __str__(self):
        return self.title_text
