from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPostModel
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User


def about(request):
    return render(request, "blog_app/about.html")


class Home(ListView):
    model = BlogPostModel
    template_name = "blog_app/home.html"
    context_object_name = "posts"
    ordering = ['-posted_date']
    paginate_by = 5


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


class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BlogPostModel
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class AllPostOfUser(ListView):
    model = BlogPostModel
    template_name = "blog_app/all_post_of_user.html"
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return BlogPostModel.objects.filter(author=user).order_by("-posted_date")
