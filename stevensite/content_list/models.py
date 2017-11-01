from django.db import models

class Article(models.Model):
    title_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title_text


