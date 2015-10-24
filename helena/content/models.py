from django.db import models

from helpers.service import image_path


class Genres(models.Model):

    """ class with genres model """

    def get_image_path(instace, filename):
        return image_path(instace, filename, directory='genres')

    title = models.CharField(verbose_name='Заголовок', max_length=200)
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Изображение пример', upload_to=get_image_path)

    def __str__(self):
        return self.title
