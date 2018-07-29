from django.db import models

class Article(models.Model):
    name_text = models.CharField(max_length=32, default='name', primary_key=True)
    title_text = models.CharField(max_length=256, default='title')
    subtitle_text = models.CharField(max_length=256, default='subtitle')
    pub_date = models.DateTimeField('date published')
    content_text = models.TextField()
    link_text = models.CharField(max_length=256, blank=True)
    foreword_text = models.CharField(max_length=256, blank=True, default='')
    hidden_text = models.TextField(blank=True)

    def __str__(self):
        return self.title_text

