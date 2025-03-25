from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class Issue(models.Model):
    title = models.CharField(max_length=200)
    number = models.PositiveIntegerField(unique=True)
    publication_date = models.DateField()
    description = models.TextField()
    is_published = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Numéro {self.number} - {self.title}"

class Article(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('under_review', 'Under review'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.SET_NULL, null=True, blank=True)
    abstract = models.TextField()
    keywords = models.CharField(max_length=255)
    domain = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    submission_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    document = models.FileField(upload_to='articles/')
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return self.title

