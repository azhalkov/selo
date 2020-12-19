from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """Изменить в админке название приложения на русский язык
    добавить  dom/__init__   default_app_config = 'dom.apps.DomConfig'"""
    name = 'accounts'
    verbose_name = 'Аккаунт'
