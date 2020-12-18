from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Categori, DomDokument

class CategoriAdmin(admin.ModelAdmin):
    model = Categori
    list_display = ('name', 'description', 'slug')
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Categori, CategoriAdmin)


class DomDokumentAdmin(admin.ModelAdmin):
    model = Categori
    list_display = ('name_document', 'filedom', 'datepub', 'slug')
    prepopulated_fields = {"slug": ("name_document",)}


admin.site.register(DomDokument, DomDokumentAdmin)