from django.shortcuts import get_object_or_404, redirect
from blog_app.models import Category, Post
from django.shortcuts import render
from blog_app.forms import PostForm, SearchForm, CategoryForm
from pytils.translit import slugify


def index(request):
    search_form = SearchForm(request.GET)
    posts = Post.objects.filter(published=True)
    if search_form.is_valid():
        query = search_form.cleaned_data.get('query')
        posts = posts.filter(title__icontains=query)
        posts = posts[:5]
    context = {
        'posts': posts,
        'search_form': search_form
    }
    return render(request, 'blog/index.html', context)

def posts_list(request):
    posts = Post.objects.filter(published=True)

    content = '<h1>Опубликованные статьи</h1><br><br>'
    for post in posts:
        content += f'<a href="/posts/{post.id}">{post.title}</a> ({post.created_at})<br>'
    context = {'posts': posts}

    return render(request, 'blog/posts_list.html', context)

def posts_detail(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    post.increase_views_count()
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


def post_create(request):
    if request.method == 'POST':
        form = PostForm(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.slug = slugify(post.title)
            post.save()
            return redirect('blog:index_page')
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', context={'form':form})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.slug = slugify(category.title)
            category.save()
            return redirect('blog:index_page')
    else:
        form = CategoryForm()
    return render(request, 'blog/category_create.html', context = {'form':form})

def post_edit(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    form = PostForm(request.POST or None, instance=post)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('blog:posts_detail', post_slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', context={'form':form, 'post':post})
