from django.test import TransactionTestCase
from content.models import Genres


class GenresTestCase(TransactionTestCase):

    """ Tests for content model genres """

    def test_verbose_names(self):
        """ Test verbose name for model """
        # create verbose_names dict with correct name of fields
        verbose_names = dict(
            title='Заголовок', description='Описание', image='Изображение пример', )
        # create counter to check correct number of fields
        counter = 0
        # cycle check verbose names
        for field in verbose_names:
            field = self.model._meta.get_field_by_name(field)[0]
            counter += 1
            self.assertEquals(field.verbose_name, verbose_names[field.name])
        # check is counter has a correct value 1
        self.assertEquals(counter, 3)
        # check class verbose name
        self.assertEquals(self.model._meta.verbose_name, 'жанр')
        self.assertEquals(self.model._meta.verbose_name_plural, 'жанры')
