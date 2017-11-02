from django.db import models

class Article(models.Model):
    category_text = models.CharField(max_length=50, default='category')
    name_text = models.CharField(max_length=20, default='code_name')
    title_text = models.CharField(max_length=200, default='title')
    subtitle_text = models.CharField(max_length=200, default='subtitle')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title_text


