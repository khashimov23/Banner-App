from django.apps import AppConfig


class BannerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'banner'

    def ready(self):
        from . import signals 