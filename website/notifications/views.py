from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Notification

@login_required
def user_notifications(request):
    notifications = Notification.objects.filter(recipient=request.user).order_by('-created_at')
    unread = notifications.filter(is_read=False)
    
    # Marquer comme lues lorsqu'elles sont visualisées
    unread.update(is_read=True)
    
    return render(request, 'notifications/list.html', {'notifications': notifications})

# Create your views here.
