from django.db import models

class Article(models.Model):
    title_text = models.CharField(max_length=200, default='title')
    name_text = models.CharField(max_length=20, default='name')
    subtitle_text = models.CharField(max_length=200, default='subtitle')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title_text


class LinkToPostStatic(models.Model):
    name_text = models.CharField(max_length=50, default='name', primary_key=True)
    link_text = models.CharField(max_length=200, default='posts/static_html/')
    title_text = models.CharField(max_length=200, default='title')

    def __str__(self):
        return self.title_text


# How to use inheritance here for LinkToPostStatic?
#class QuickLink(models.Model):
#    link_text = models.CharField(max_length=200, default='posts/static_html/quick_link/', primary_key=True)
#    title_text = models.CharField(max_length=200, default='title')
#
#    def __str__(self):
#        return self.title_text


class PdfFile(models.Model):
    name_text = models.CharField(max_length=200)
    link_text = models.CharField(max_length=200, default='posts/static_pdf/', primary_key=True)
    title_text = models.CharField(max_length=200, default='title')

    def __str__(self):
        return self.title_text

