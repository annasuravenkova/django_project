from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from blog_app.models import Category
from django.shortcuts import render

from blog_app.models import Post

def index(request):
    posts = Post.objects.filter(published=True)[:5]

    context = {'posts': posts}
    return render(request, 'blog/index.html', context)

def posts_list(request):
    posts = Post.objects.filter(published=True)

    content = '<h1>Опубликованные статьи</h1><br><br>'
    for post in posts:
        content += f'<a href="/posts/{post.slug}/">{post.title}</a> ({post.created_at})<br>'

    return HttpResponse(content)

def posts_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context)

def categories_list(request):
    categories = Category.objects.all()
    content = '<ul>'
    for category in categories:
        content += f'''
        <li>{category.title}</li><ul><br><br>
        '''
    content += '</ul>'
    return HttpResponse(content)

def categories_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    content = f"<h1>{category.title}</h1>"
    posts = Post.objects.filter(category=category, published=True)
    for post in posts:
       content += f'''<a href="/posts/{post.slug}/">{post.title}</a><br><br>'''
    return HttpResponse(content)
