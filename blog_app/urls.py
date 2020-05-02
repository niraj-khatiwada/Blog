from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home.as_view(), name="blog-home"),
    path("about/", views.about, name="blog-about"),
    path("post/<int:pk>/", views.PostDetail.as_view(), name="post-detail"),
    path("post/create/", views.PostCreate.as_view(), name="create-post"),
    path("post/<int:pk>/update", views.PostUpdate.as_view(), name="update-post"),
]
