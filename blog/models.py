from django.db import models

NULLABLE = {'blank': True, 'null': True}


class BlogEntry(models.Model):
    heading = models.CharField(max_length=200, verbose_name='заголовок')
    slug = models.CharField(max_length=100, verbose_name='slug', **NULLABLE)
    content = models.CharField(max_length=500, verbose_name='содержимое')
    image = models.ImageField(upload_to='blog/', verbose_name='превью', **NULLABLE)
    created_at = models.DateField(auto_now_add=True, verbose_name='дата создания')
    is_published = models.BooleanField(default=True, verbose_name='признак публикации')
    views_count = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return f'{self.heading}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
