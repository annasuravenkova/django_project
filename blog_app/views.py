from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from blog_app.models import Post
from .models import Category

def index(request):
    posts = Post.objects.filter(published=True)[:5]

    context = {'posts': posts}
    return render(request, 'blog/index.html', context)

def posts_list(request):
    posts = Post.objects.filter(published=True)

    content = '<h1>Опубликованные статьи</h1><br><br>'
    for post in posts:
        content += f'<a href="/posts/{post.id}">{post.title}</a> ({post.created_at})<br>'

    return HttpResponse(content)

def posts_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context)


def categories_list(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'blog/categories_list.html', context)


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category, published=True)
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'blog/category_detail.html', context)
