from django.urls import path
from blog_app import views

app_name = 'blog'

urlpatterns = [
    path("", views.index, name="index_page"),
    path("posts/", views.posts_list, name="posts_list"),
    path('posts/<int:post_id>/', views.posts_detail, name="posts_detail")
]
