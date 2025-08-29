from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from django.views.generic import View
from . import models

# Create your views here.
class Blog(View):
    
    def get(self, request):
        categoria_id = request.GET.get("categoria")
        search_query = request.GET.get("q")
        page_number = request.GET.get("page", 1)  # pega a página da query string, padrão 1
        
        posts = models.Post.objects.all()
        
        if categoria_id:
            posts = posts.filter(category_id=categoria_id)
        
        if search_query:
            posts = posts.filter(title__icontains=search_query)
        
        paginator = Paginator(posts, 2)
        page_obj = paginator.get_page(page_number)  # retorna a página atual
        
        context = {
            "page_obj": page_obj,                  # objeto paginado
            "posts": page_obj.object_list,         # posts da página atual
            "categories": models.PostCategory.objects.all(),
            "categoria_id": categoria_id,
            "search_query": search_query,
        }
        return render(request, "blog/blog.html", context)

    
    def post(self, request):
        
        context = {
            
        }
        return render(request, 'blog/blog.html', context)
    
class Post(View):
    
    def get(self, request, pk):
        post = get_object_or_404(models.Post, pk=pk)

        try:
            post_anterior = models.Post.objects.filter(pk__lt=pk).order_by('-pk').first()
        except Post.DoesNotExist:
            post_anterior = None

        try:
            post_proximo = models.Post.objects.filter(pk__gt=pk).order_by('pk').first()
        except Post.DoesNotExist:
            post_proximo = None


        context = {
            "post": post,
            "previous_post": post_anterior,
            "next_post": post_proximo,
            "posts": models.Post.objects.all(),
            "categories": models.PostCategory.objects.all()
        }
        return render(request, "blog/post.html", context)
    
    def post(self, request):
        
        context = {
            
        }
        return render(request, 'blog/blog.html', context)