from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ArticleSubmissionForm
from notifications.models import Notification
from django.contrib.auth import get_user_model
from django.contrib.admin.views.decorators import staff_member_required
from .models import Article

User = get_user_model()

@login_required
def submit_article(request):
    if request.method == 'POST':
        form = ArticleSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            
            # Notifier les administrateurs
            admins = User.objects.filter(is_staff=True)
            for admin in admins:
                Notification.objects.create(
                    recipient=admin,
                    message=f"Nouvel article soumis: {article.title}",
                    related_article=article
                )
            
            messages.success(request, 'Votre article a été soumis avec succès!')
            return redirect('home')
    else:
        form = ArticleSubmissionForm()
    
    return render(request, 'articles/submit_article.html', {'form': form})


@staff_member_required
def review_article(request, article_id):
    article = Article.objects.get(id=article_id)
    
    if request.method == 'POST':
        new_status = request.POST.get('status')
        article.status = new_status
        article.save()
        
        # Notifier l'auteur
        Notification.objects.create(
            recipient=article.author,
            message=f"Votre article '{article.title}' est maintenant {article.get_status_display()}",
            related_article=article
        )
        
        return redirect('article_dashboard')
    
    return render(request, 'articles/admin/review.html', {'article': article})
