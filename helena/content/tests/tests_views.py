from django.core.urlresolvers import reverse

from django.test import TransactionTestCase


class ContentViewTestCase(TransactionTestCase):

    """ Tests for content view check """

    def setUp(self):
        self.url_index = reverse('content:index')
        self.url_genres = reverse('content:genres')
        self.url_gallery = reverse('content:gallery')
        self.url_contacts = reverse('content:contacts')

    def test_url_resolved(self):
        """ Check url reverse correct """
        self.assertEqual(self.url_index, '/')
        self.assertEqual(self.url_genres, '/genres')
        self.assertEqual(self.url_gallery, '/gallery')
        self.assertEqual(self.url_contacts, '/contacts')

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

    def test_contacts_page(self):
        """ Get 200 on contacts page """
        response = self.client.get(self.url_contacts)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            '<li><a href="%s" class=\'active\'>Контакты</a></li>' % self.url_contacts,
            response.content.decode('utf-8'))

    def test_contacts_page_post(self):
        """ Correct send msg """
        response = self.client.post(self.url_contacts, data=dict(
            name='Пользователь', email='user@e.co', message='Здравствуйте, хочу заказать фотосессию'))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(response.url)
        self.assertIn(
            '<li><a href="%s" class=\'active\'>Контакты</a></li>' % self.url_contacts,
            response.content.decode('utf-8'))
