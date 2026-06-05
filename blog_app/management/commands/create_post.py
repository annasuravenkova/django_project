from django.core.management import BaseCommand
from blog_app.models import Post
from pytils.translit import slugify

class Command(BaseCommand):
    #def add_arguments(self, parser):
        #parser.add_argument('--title', type=str)
        #parser.add_argument('--content', type=str)

    def handle(self, *args, **options):
        title = input("Введите заголовок поста: ")
        title_slug = slugify(title)

        content = input("Введите текст поста ")

        Post.objects.create(title=title,content=content, slug=title_slug)
        self.stdout.write("Пост создан")
