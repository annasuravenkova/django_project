from django.core.management import BaseCommand
from blog_app.models import Post

class Command(BaseCommand):
    def handle(self, *args, **options):
        post_id = int(input('Введите id поста: '))
        try:
            post = Post.objects.get(id=post_id)
            post.delete()
            self.stdout.write("Пост удален")
        except Post.DoesNotExist:
            self.stdout.write("Пост не найден")
