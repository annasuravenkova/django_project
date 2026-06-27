from django.contrib.auth.models import User
from django.db import models
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    social_link = models.URLField(blank=True)
    objects = models.Manager()
    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True,
        null=True,
        verbose_name='Аватар'
    )

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f"Профиль {self.user.username}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.avatar:
            image = Image.open(self.avatar.path)
            if image.width > 300 or image.height > 300:
                output_size = (300, 300)
                image.thumbnail(output_size)
                image.save(self.avatar.path)
