# Local settings
import os
from os.path import join

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Turn debug mode on
DEBUG = True
TEMPLATE_DEBUG = True

# Database connection
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(BASE_DIR, 'helena.sqlite3'),
    }
}

DEFAULT_FROM_EMAIL = 'a@bc.def'
DEFAULT_TO_EMAIL = 'b@bc.def'
