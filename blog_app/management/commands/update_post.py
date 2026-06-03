from django.core.management import BaseCommand
from blog_app.models import Post

class Command(BaseCommand):
    def handle(self, *args, **options):
        post_id = int(input('Введите id поста: '))
        new_title = (input('Введите новый заголовок поста: '))
        try:
            post = Post.objects.get(id=post_id)
            post.title = new_title
            post.save()
        except Post.DoesNotExist:
            self.stdout.write("Пост не найден")
