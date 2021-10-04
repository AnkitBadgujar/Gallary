from django.apps import AppConfig

from Gallery.settings import DEFAULT_AUTO_FIELD


class PhotosConfig(AppConfig):
    DEFAULT_AUTO_FIELD = id = 'django.db.models.Autofield'
    name = 'photos'
