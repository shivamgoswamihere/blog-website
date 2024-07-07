from django.shortcuts import render
from .models import Post
# Create your views here.

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, "django_app/index.html", context)

def about(request):
    return render(request,"django_app/about.html", {"title": "about"})