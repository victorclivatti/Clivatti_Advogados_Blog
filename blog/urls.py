from django.urls import path
from . import views

urlpatterns = [
    path("", views.Blog.as_view(), name="blog"),
    path("post/<int:pk>", views.Post.as_view(), name="post"),
]