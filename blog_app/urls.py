from django.urls import path
from blog_app import views
from django.views.generic import TemplateView

app_name = 'blog'

urlpatterns = [
    path("", views.IndexView.as_view(), name="index_page"),
    path("posts/", views.PostListView.as_view(), name="posts_list"),
    path('posts/create/', views.PostCreateView.as_view(), name="post_create"),
    path('posts/<slug:post_slug>/', views.PostDetailView.as_view(), name="posts_detail"),
    path('posts/<slug:post_slug>/edit/', views.PostUpdateView.as_view(), name="post_edit"),
    path('posts/<slug:post_slug>/delete/', views.PostDeleteView.as_view(), name="post_delete"),
    path("categories/", views.CategoriesListView.as_view(), name="categories_list"),
    path('category/<int:category_id>/', views.CategoryDetailView.as_view(), name="category_detail"),
    path('categories/create/', views.CategoryCreateView.as_view(), name="category_create"),
    path('about/', TemplateView.as_view(template_name='blog/about.html'), name='about'),
]
