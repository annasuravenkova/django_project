from django.core.management import BaseCommand
from blog_app.models import Post

class Command(BaseCommand):
    def print_published_posts(self):
        published_posts = Post.objects.filter(published=True)

        if not published_posts.exists():
            self.stdout.write(self.style.WARNING('Нет опубликованных статей.'))
            return

        self.stdout.write("Опубликованные посты")
        for post in published_posts:
            self.stdout.write(f'{post.id}: {post.title} - {post.created_at:%Y-%m-%d}')

    def handle(self, *args, **options):
        self.print_published_posts()
