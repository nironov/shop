import os
from django.conf import settings


def upload_favicon(instance, filename):
    name, ext = os.path.splitext(filename.lower())
    filename = f'favicon{ext}'

    upload_dir = 'settings'
    path_to_upload_dir = f'{settings.BASE_DIR}/media/{upload_dir}'

    if os.path.isdir(path_to_upload_dir):
        if filename in os.listdir(path_to_upload_dir):
            os.remove(f'{path_to_upload_dir}/{filename}')
    return f'{upload_dir}/{filename}'