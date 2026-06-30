from django.contrib.auth.models import User
from django.db import models
from PIL import Image

class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название категории")
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    slug = models.SlugField(unique=True)
    content = models.TextField(verbose_name="Текст статьи")
    published = models.BooleanField(default=False, verbose_name="Статус публикации")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name="Автор", null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    views_count = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="posts", verbose_name="Категория", null=True)
    image = models.ImageField(upload_to='posts/', blank=True, null=True, verbose_name='Обложка')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']

    def increase_views_count(self):
        self.views_count += 1
        self.save()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            image = Image.open(self.image.path)
            if image.width > 1200 or image.height > 1200:
                output_size = (1200, 1200)
                image.thumbnail(output_size)
                image.save(self.image.path)
