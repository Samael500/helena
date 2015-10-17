from django.conf import settings

def custom_variables_processor(request):
    """ Extend the template with custom variables """
    return dict(SOCIAL_LINKS=settings.SOCIAL_LINKS)
