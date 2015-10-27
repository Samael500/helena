import os
import uuid

from datetime import datetime
from hashlib import md5


def image_path(instance, filename, directory=None):
    """ Path to image *directory*/abcdef0123456789abcdef0123456789.jpg """
    basename, ext = os.path.splitext(filename)
    hashed_name = md5(
        '{0}{1}{2}'.format(uuid.uuid4(), filename, datetime.now()).encode('utf-8')).hexdigest()
    return os.path.join(directory, hashed_name + ext)
