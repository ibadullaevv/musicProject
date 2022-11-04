from django.db import models


class Article(models.Model):
    author = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    urlToImage = models.ImageField(upload_to='images/news/')
