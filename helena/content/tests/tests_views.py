from django.core.urlresolvers import reverse

from django.test import TransactionTestCase


class ContentViewTestCase(TransactionTestCase):

    """ Tests for content view check """

    def setUp(self):
        self.url_index = reverse('content:index')
        self.url_genres = reverse('content:genres')
        self.url_gallery = reverse('content:gallery')

    def test_url_resolved(self):
        """ Check url reverse correct """
        self.assertEqual(self.url_index, '/')
        self.assertEqual(self.url_genres, '/genres')
        self.assertEqual(self.url_gallery, '/gallery')

    def test_index_page(self):
        """ Get 200 on index page """
        response = self.client.get(self.url_index)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Сохраните лучшие моменты...', response.content.decode('utf-8'))

    def test_genres_page(self):
        """ Get 200 on genres page """
        response = self.client.get(self.url_genres)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            '<li><a href="%s" class=\'active\'>Жанры</a></li>' % self.url_genres,
            response.content.decode('utf-8'))

    def test_gallery_page(self):
        """ Get 200 on gallery page """
        response = self.client.get(self.url_gallery)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            '<li><a href="%s" class=\'active\'>Галерея</a></li>' % self.url_gallery,
            response.content.decode('utf-8'))
