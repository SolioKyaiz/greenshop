from django.db import models
from account.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os

class Post(models.Model):
    owner = models.ForeignKey(
        to = User,
        on_delete=models.CASCADE,
        related_name = 'posts',
        verbose_name='Автор',
    )

    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'

    )
    description = models.CharField(
        max_length=255,
        verbose_name='Краткое описание'
    )
    content = models.TextField(verbose_name='Контент')

    published_at = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

class PostImage(models.Model):
    post = models.ForeignKey(
        to = Post,
        on_delete=models.CASCADE,
        related_name = 'images',
        verbose_name='Рисунок',
    )
    image = models.ImageField(
        upload_to='images/posts/',
    )

    class Meta:
        verbose_name = 'Рисунок статьи'
        verbose_name_plural = 'Рисунки статей'

@receiver(post_delete, sender=Post)
def plant_delete_receiver(sender, instance, **kwargs):
    if hasattr(instance,'images'):
        for image in instance.images.all():
            if os.path.exists(image.image.path):
                os.remove(image.image.path)
            image.delete()