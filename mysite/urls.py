# mysite/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView


"""Изменить заголовок в админке(администрирование django)"""
admin.site.site_header = 'НЕДВИЖИМОСТЬ'

urlpatterns = [
    path('', TemplateView.as_view(template_name='dom/index.html'), name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('dom/', include('dom.urls')),
    path('todo/', include('todolist.urls')),
    path('polls/', include('polls.urls')),
    path('uroki/', include('urokipy.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)