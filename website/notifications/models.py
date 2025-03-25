from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    related_article = models.ForeignKey('articles.Article', on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f"Notification pour {self.recipient.email}"
