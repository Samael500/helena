from django.views.generic import TemplateView, ListView
from content.models import Genres, Galleries


class IndexView(TemplateView):

    """ simple template for index page """

    template_name = 'index.html'


class GenresView(ListView):

    """ list with genres """

    model = Genres
    template_name = 'genres.html'


class GalleryView(ListView):

    """ list with gallery page """

    model = Galleries
    paginate_by = 25
    template_name = 'gallery.html'
