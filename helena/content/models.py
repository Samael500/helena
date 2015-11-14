from django.db import models

from helpers.service import image_path


class ImgWithDescr(models.Model):

    """ class with genres model """

    directory = None

    def get_image_path(instace, filename):
        return image_path(instace, filename, directory=instace.directory)

    title = models.CharField(verbose_name='Заголовок', max_length=200)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    image = models.ImageField(verbose_name='Изображение', upload_to=get_image_path, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class Genres(ImgWithDescr):

    """ class with genres model """

    directory = 'genres'

    class Meta:
        verbose_name = 'жанр'
        verbose_name_plural = 'жанры'


class Galleries(ImgWithDescr):

    """ class with gallery model """

    directory = 'gallery'
    external_img = models.URLField(verbose_name='Изображение во внешнем источнике', blank=True, null=True)

    @property
    def img_src(self):
        """ return external img url or self file img """
        return self.external_img or self.image

    @property
    def img_url(self):
        """ return external img url or self file img """
        return self.external_img or self.image.url

    class Meta:
        verbose_name = 'изображение в галлерее'
        verbose_name_plural = 'изображения в галлерее'
