from django.apps import AppConfig


class ClickConfig(AppConfig):
    name = 'click'

    def ready(self):
        import click.signals