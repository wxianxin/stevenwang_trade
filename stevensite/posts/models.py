from django.db import models

class Article(models.Model):
    name_text = models.CharField(max_length=20, default='name', primary_key=True)
    title_text = models.CharField(max_length=200, default='title')
    subtitle_text = models.CharField(max_length=200, default='subtitle')
    pub_date = models.DateTimeField('date published')
    content_text = models.TextField()

    def __str__(self):
        return self.title_text

