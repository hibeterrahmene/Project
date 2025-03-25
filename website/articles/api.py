from rest_framework import viewsets, permissions
from .models import Article, Issue
from .serializers import ArticleSerializer, IssueSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.filter(status='accepted')
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.filter(is_published=True)
    serializer_class = IssueSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]