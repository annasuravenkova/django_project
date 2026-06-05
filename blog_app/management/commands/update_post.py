from django.core.management import BaseCommand
from blog_app.models import Post

class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            post_id = int(input('Введите id поста: '))
        except ValueError:
            self.stdout.write("Вы ввели некорректные данные. Нужно ввести число!")
            return
        new_title = input('Введите новый заголовок поста: ')
        try:
            post = Post.objects.get(id=post_id)
            post.title = new_title
            post.save()
        except Post.DoesNotExist:
            self.stdout.write("Пост не найден")
