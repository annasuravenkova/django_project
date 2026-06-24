from blog_app.models import Category, Post
from django.shortcuts import render
from blog_app.forms import PostForm, SearchForm, CategoryForm
from pytils.translit import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


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

# def posts_list(request):
#     posts = Post.objects.filter(published=True)
#
#     content = '<h1>Опубликованные статьи</h1><br><br>'
#     for post in posts:
#         content += f'<a href="/posts/{post.id}">{post.title}</a> ({post.created_at})<br>'
#     context = {'posts': posts}
#
#     return render(request, 'blog/posts_list.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts'
    paginate_by = 5
    def get_queryset(self):
        return Post.objects.filter(published=True)

# def posts_detail(request, post_slug):
#     post = get_object_or_404(Post, slug=post_slug)
#     post.increase_views_count()
#     context = {'post': post}
#     return render(request, 'blog/post_detail.html', context)

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    slug_url_kwarg = 'post_slug'

    def get_object(self, queryset=None):
        post = super().get_object(queryset=queryset)
        post.increase_views_count()
        return post

# def categories_list(request):
#     categories = Category.objects.all()
#     context = {
#         'categories': categories
#     }
#     return render(request, 'blog/categories_list.html', context)

class CategoriesListView(ListView):
    model = Category
    template_name = 'blog/categories_list.html'
    context_object_name = 'categories'

#
# def category_detail(request, category_id):
#     category = get_object_or_404(Category, id=category_id)
#     posts = Post.objects.filter(category=category, published=True)
#     context = {
#         'category': category,
#         'posts': posts
#     }
#     return render(request, 'blog/category_detail.html', context)

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'blog/category_detail.html'
    context_object_name = 'category'
    pk_url_kwarg = 'category_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(category=self.object, published=True)
        return context



# def post_create(request):
#     if request.method == 'POST':
#         form = PostForm(data=request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.slug = slugify(post.title)
#             post.save()
#             return redirect('blog:index_page')
#     else:
#         form = PostForm()
#     return render(request, 'blog/post_create.html', context={'form':form})
#
# def category_create(request):
#     if request.method == 'POST':
#         form = CategoryForm(data=request.POST)
#         if form.is_valid():
#             category = form.save(commit=False)
#             category.slug = slugify(category.title)
#             category.save()
#             return redirect('blog:index_page')
#     else:
#         form = CategoryForm()
#     return render(request, 'blog/category_create.html', context = {'form':form})

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'blog/category_create.html'
    success_url = reverse_lazy('blog:index_page')
    def form_valid(self, form):
        category = form.save(commit=False)
        category.slug = slugify(category.title)
        category.save()
        return super().form_valid(form)


class PostFormBase:
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('blog:index_page')

class PostCreateView(PostFormBase, CreateView):
    template_name = 'blog/post_create.html'

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)

# def post_edit(request, post_slug):
#     post = get_object_or_404(Post, slug=post_slug)
#     form = PostForm(request.POST or None, instance=post)
#     if request.method == "POST" and form.is_valid():
#         form.save()
#         return redirect('blog:posts_detail', post_slug=post.slug)
#     return render(request, 'blog/post_edit.html', context={'form':form, 'post':post})

class PostUpdateView(PostFormBase, UpdateView):
    template_name = 'blog/post_edit.html'
    slug_url_kwarg = 'post_slug'

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('blog:index_page')
    slug_url_kwarg = 'post_slug'
