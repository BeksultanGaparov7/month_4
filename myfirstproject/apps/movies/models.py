from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=120, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='movies/',verbose_name='Изображение')
    year = models.IntegerField(verbose_name='Год выпуска')
    rating = models.FloatField(verbose_name='Рейтинг(0-10)')

    def __str__(self):
        return self.title
