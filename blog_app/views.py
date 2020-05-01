from django.shortcuts import render
from .models import BlogPostModel


def home(request):
    context = {
        'posts': BlogPostModel.objects.all()
    }
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html")
