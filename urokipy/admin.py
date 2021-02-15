from django.contrib import admin
from . models import Karta


class KartaAdmin(admin.ModelAdmin):
    fields = ['title', 'image', 'alt', 'text', 'links', 'button_text', 'tags', ]

admin.site.register(Karta, KartaAdmin)