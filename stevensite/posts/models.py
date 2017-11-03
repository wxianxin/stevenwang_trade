from django.db import models

class Post(models.Model):
    name_text = models.CharField(max_length=20, default='name')
    title_text = models.CharField(max_length=200, default='title')
    subtitle_text = models.CharField(max_length=200, default='subtitle')
    author_text = models.CharField(max_length=50, default='author_name')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title_text

# Create your models here.
