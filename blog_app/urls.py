from django.urls import path
from blog_app import views

app_name = 'blog'

urlpatterns = [
    path("", views.index, name="index_page"),
    path("posts/", views.posts_list, name="posts_list"),
    path('posts/create/', views.post_create, name="post_create"),
    path('posts/<slug:post_slug>/', views.posts_detail, name="posts_detail"),
    path("categories/", views.categories_list, name="categories_list"),
    path('category/<int:category_id>/', views.category_detail, name="category_detail"),
    path('categories/create/', views.category_create, name="category_create"),
    #path('posts/<slug:post_slug>/edit/', views.post_edit, name="post_edit"),
]
