from django.core.management import BaseCommand
from blog_app.models import Post
from django.utils.text import slugify

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--title', type=str)
        parser.add_argument('--content', type=str)
        #parser.add_argument('--author', type=str, required=False)

    def handle(self, *args, **options):
        title = options['title']
        title_slug = slugify(title, allow_unicode=True)

        Post.objects.create(title=options['title'],content=options['content'], slug=title_slug)
