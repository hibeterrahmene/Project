from rest_framework import serializers
from .models import Article, Issue

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'author', 'abstract', 'keywords', 'domain', 'category', 'submission_date']

class IssueSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True, read_only=True)
    
    class Meta:
        model = Issue
        fields = ['id', 'title', 'number', 'publication_date', 'description', 'articles']