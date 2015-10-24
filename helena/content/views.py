from django.views.generic import TemplateView


class IndexView(TemplateView):

    """ simple template for index page """

    template_name = 'index.html'


class GenersView(TemplateView):

    """ list with geners """

    template_name = 'geners.html'

