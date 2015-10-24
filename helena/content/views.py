from django.views.generic import TemplateView, ListView
from content.models import Genres


class IndexView(TemplateView):

    """ simple template for index page """

    template_name = 'index.html'


class GenresView(ListView):

    """ list with genres """

    model = Genres
    template_name = 'genres.html'


class GalleryView(TemplateView):

    """ simple template for gallery page """

    template_name = 'gallery.html'
