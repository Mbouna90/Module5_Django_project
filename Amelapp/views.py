from django.shortcuts import render
from django.utils import timezone
from .models import Post

def home(request):
    return render(request, 'Amelapp/home.html')

def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()
    ).order_by('published_date')

    return render(request, 'Amelapp/post_list.html', {'posts': posts})