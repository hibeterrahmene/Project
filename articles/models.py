from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    resume = models.CharField(max_length=300)
    review_number = models.CharField(max_length=20)
