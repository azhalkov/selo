# partner/urls
from django.template import Template
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView
from urokipy.views import KartaListView

from . import views


urlpatterns = [

    path('', TemplateView.as_view(template_name='partner/home.html'), name='uroki'),
    # path('spisok/', KartaListView.as_view(template_name='urokipy/stroki.html'), name='spisok'),

]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)