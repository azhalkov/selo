from django.contrib import admin
from . models import Karta, Bulma


class KartaAdmin(admin.ModelAdmin):
    fields = ['title', 'image', 'alt', 'text', 'links', 'button_text', 'tags', ]

admin.site.register(Karta, KartaAdmin)


class BulmaAdmin(admin.ModelAdmin):
    fields = ['title', 'image', 'alt', 'text', 'links', 'button_text', 'tags', ]

admin.site.register(Bulma, BulmaAdmin)