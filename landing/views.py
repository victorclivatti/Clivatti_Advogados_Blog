from django.shortcuts import render
from blog.models import Post

def home(request):
    posts = Post.objects.all()
    last_four_posts = posts[:5]

    context = {
        'last_four_posts': last_four_posts
    }

    return render(request, "landing/home.html", context)