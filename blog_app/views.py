from django.shortcuts import render, redirect
from .models import BlogPostModel
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView


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


class PostCreate(LoginRequiredMixin, CreateView):
    model = BlogPostModel
    fields = ["post_title", "post_text"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BlogPostModel
    fields = ["post_title", "post_text"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
