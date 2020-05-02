from django.shortcuts import render
from .models import BlogPostModel
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, DetailView


# def home(request):
#     context = {
#         'posts': BlogPostModel.objects.all()
#     }
#     return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html")

# @login_required()
# def create_post(request):
#     if request.method == "POST":


class Home(ListView):
    model = BlogPostModel
    template_name = "blog_app/home.html"
    context_object_name = "posts"
    ordering = ['-posted_date']


class PostDetail(DetailView):
    model = BlogPostModel
    context_object_name = "post"
