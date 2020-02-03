from django.apps import AppConfig


class LibrarymanagerConfig(AppConfig):
    name = 'librarymanager'

    def ready(self):
        import librarymanager.signals