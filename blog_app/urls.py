from django.urls import path
from blog_app import views

app_name = 'blog'

urlpatterns = [
    path("", views.index, name="index_page"),
    path("posts/", views.posts_list, name="posts_list"),
    path('posts/<slug:post_slug>/', views.posts_detail, name="posts_detail"),
    path("categories/", views.categories_list, name="categories_list"),
    path('category/<int:category_id>/', views.category_detail, name="category_detail")
]
