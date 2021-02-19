""" partner/apps """
from django.apps import AppConfig


class PartnerConfig(AppConfig):
    name = 'partner'
    verbose_name = 'Партнеры'  # Меняем название приложения в админке необходимо добавить __init__
                               # этого приложения default_app_config = 'partner.apps.PartnerConfig'

