from django.apps import AppConfig


"""Изменить в админке название приложения на русский язык
добавить  dom/__init__   default_app_config = 'dom.apps.DomConfig'"""

class DomConfig(AppConfig):
    name = 'dom'
    verbose_name = 'Строения'
